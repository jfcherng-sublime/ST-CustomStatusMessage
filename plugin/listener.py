import sublime
import sublime_plugin

from .constant import PLUGIN_NAME, STATUS_MSG_KEY
from .utils import get_plugin_setting, get_template_variables, is_regular_view


class CustomStatusMessageListener(sublime_plugin.ViewEventListener):
    def __init__(self, view: sublime.View, *args, **kwargs) -> None:
        super().__init__(view, *args, **kwargs)
        self.v_settings = view.settings()
        self.v_settings.add_on_change(PLUGIN_NAME, self._work)

    def __del__(self) -> None:
        self.v_settings.clear_on_change(PLUGIN_NAME)

    def _is_enabled(self, view: sublime.View) -> bool:
        return bool(get_plugin_setting("enabled") and is_regular_view(view) and len(view.sel()) == 1)

    def _work(self) -> None:
        if not self._is_enabled(self.view):
            self.view.erase_status(STATUS_MSG_KEY)
            return

        template = str(get_plugin_setting("template"))
        variables = get_template_variables(self.view, point=self.view.sel()[0].b)

        try:
            msg = template.format_map(variables)
        except KeyError as e:
            msg = f"[{PLUGIN_NAME}] Unknown template variable: {e}"
        except Exception as e:
            msg = f"[{PLUGIN_NAME}] Error parsing template: {e}"

        self.view.set_status(STATUS_MSG_KEY, msg)

    on_activated_async = _work
    on_selection_modified_async = _work
