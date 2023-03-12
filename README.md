# ST-CustomStatusMessage

[![Required ST Build](https://img.shields.io/badge/ST-4138+-orange.svg?style=flat-square&logo=sublime-text)](https://www.sublimetext.com)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/jfcherng-sublime/ST-CustomStatusMessage/python.yml?branch=st4&style=flat-square)](https://github.com/jfcherng-sublime/ST-CustomStatusMessage/actions)
[![Package Control](https://img.shields.io/packagecontrol/dt/CustomStatusMessage?style=flat-square)](https://packagecontrol.io/packages/CustomStatusMessage)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/jfcherng-sublime/ST-CustomStatusMessage?style=flat-square&logo=github)](https://github.com/jfcherng-sublime/ST-CustomStatusMessage/tags)
[![Project license](https://img.shields.io/github/license/jfcherng-sublime/ST-CustomStatusMessage?style=flat-square&logo=github)](https://github.com/jfcherng-sublime/ST-CustomStatusMessage/blob/st4/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jfcherng-sublime/ST-CustomStatusMessage?style=flat-square&logo=github)](https://github.com/jfcherng-sublime/ST-CustomStatusMessage/stargazers)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-blue.svg?style=flat-square&logo=paypal)](https://www.paypal.me/jfcherng/5usd)

This plugin sets a custom message in the status bar.

## Important Notice

This plugin is unmaintained because it's not possible to do it perfect due to API limitations.

## Installation

This package is available on [Package Control][package-control] by the name of [CustomStatusMessage][customstatusmessage].

## Usage

In plugin settings (`Preferences` » `Package Settings` » `CustomStatusMessage` » `Settings`),

- Set `"enabled": true,` to enable this plugin.
- Set your wanted status message template such as `"template": "Ln {row}, Col {col}",`.

In Sublime Text settings (`Preferences` » `Settings`),

- Set `"show_line_column": "disabled",` to hide the default line/column status.

### Template Variables

| Variable       | Description                                        |
| -------------- | -------------------------------------------------- |
| `row`          | The current row number. (1-based)                  |
| `col`          | The current column number. (1-based)               |
| `row_0`        | The current row number. (0-based)                  |
| `col_0`        | The current column number. (0-based)               |
| `point`        | The current caret position.                        |
| `scope`        | The full scope at the caret position.              |
| `base_scope`   | The first part of the scope at the caret position. |
| `last_scope`   | The last part of the scope at the caret position.  |
| `buffer_id`    | The buffer ID.                                     |
| `view_id`      | The view ID.                                       |
| `sheet_id`     | The sheet ID.                                      |
| `window_id`    | The window ID.                                     |
| `encoding`     | The encoding of the current view.                  |
| `line_endings` | The line endings of the current view.              |
| `size`         | The size of the current view.                      |
| `syntax`       | The `Syntax` object of the current view.           |

[customstatusmessage]: https://packagecontrol.io/packages/CustomStatusMessage
[package-control]: https://packagecontrol.io
