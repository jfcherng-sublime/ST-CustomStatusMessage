import sublime
import sublime_plugin

from .constant import PLUGIN_NAME, STATUS_MSG_KEY
from .utils import get_plugin_setting, get_template_variables, is_regular_view


class CustomStatusMessageListener(sublime_plugin.EventListener):
    def _is_enabled(self, view: sublime.View) -> bool:
        return bool(get_plugin_setting("enabled") and is_regular_view(view) and len(view.sel()) == 1)

    def _work(self, view: sublime.View) -> None:
        if not self._is_enabled(view):
            view.erase_status(STATUS_MSG_KEY)
            return

        template = str(get_plugin_setting("template"))
        variables = get_template_variables(view, point=view.sel()[0].b)

        try:
            msg = template.format_map(variables)
        except KeyError as e:
            msg = f"[{PLUGIN_NAME}] Unknown template variable: {e}"
        except Exception as e:
            msg = f"[{PLUGIN_NAME}] Error parsing template: {e}"

        view.set_status(STATUS_MSG_KEY, msg)

    on_activated_async = _work
    on_selection_modified_async = _work
