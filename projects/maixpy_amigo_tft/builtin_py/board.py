
class board_info:
  def set(self, value=None):
    return setattr(__class__, self, value)
  def all():
    return dir(__class__)
  def get():
    return getattr(__class__, key)
  def load(self):
    for k, v in self.items():
      __class__.set(k, v)

from Maix import config
tmp = config.get_value('board_info', None)
if tmp != None:
    board_info.load(tmp)
else:
    print('[Warning] Not loaded from /flash/config.json to board_info.')
