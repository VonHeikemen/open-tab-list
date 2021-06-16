import os

import sublime
import sublime_plugin

class OtlOpenTabList(sublime_plugin.WindowCommand):
  def run(self):
    window = sublime.active_window()
    group = window.views_in_group(window.active_group())
    active_view_id = window.active_view().id()
    self.prev_in_stack = -1

    result_list = [None]
    groups = [None]

    for (i, view) in enumerate(group, start=1):
      if active_view_id == view.id():
        groups[0] = i - 1
        result_list[0] = self.get_file_info(view, i, True)
      else:
        groups.append(i - 1)
        result_list.append(self.get_file_info(view, i, False))

    def on_done(index):
      if index == -1:
        if self.prev_in_stack > -1:
          prev = groups[self.prev_in_stack]
          window.focus_view(group[prev])

        current = groups[0]
        window.focus_view(group[current])
      else:
        current = groups[0]
        window.focus_view(group[current])
        chosen = groups[index]
        window.focus_view(group[chosen])

    def preview(index):
      highlighted = groups[index]
      filename = group[highlighted].file_name()

      if filename:
        window.open_file(filename, sublime.TRANSIENT)
      else:
        self.preserve_stack_view(window)
        window.focus_view(group[highlighted])

    window.show_quick_panel(result_list, on_done, on_highlight=preview)

  def get_file_info(self, view, index, current):
    path = view.file_name()

    if path:
      parent, name = self.filepath(path)
    else:
      parent = ''
      name = view.name() or 'untitled'

    if view.is_dirty():
      mark = '+'
    else:
      mark = '-'

    if current:
      name = '[%] {} {}'.format(mark, name)
    else:
      name = '[{}] {} {}'.format(index, mark, name)

    return [name, parent]

  def filepath(self, path):
    folders = sublime.active_window().folders()
    parent, name = os.path.split(path)
    res = []

    if len(folders) > 1:
      for dir in folders:
        if dir not in parent:
          continue

        base, root = os.path.split(dir)
        res.append(os.path.join('/', parent.replace(base, "")))
    else:
        res.append(os.path.join('/', parent.replace(folders[0], "")))

    parent = "\n".join(res)[1:]
    return (parent, name)

  def preserve_stack_view(self, window):
    if self.prev_in_stack == -1:
      window.run_command('next_view_in_stack')
      _, view_index = window.get_view_index(window.active_view())
      self.prev_in_stack = view_index + 1

