from Maix import FPIOA

class fm:
  fpioa = FPIOA()

  def help():
    __class__.fpioa.help()

  def get_pin_by_function(self):
    return __class__.fpioa.get_Pin_num(self)

  def register(self, function, force=True):
    pin_used = __class__.get_pin_by_function(function)
    if pin_used == self:
      return
    if pin_used != None:
      info = "[Warning] function is used by %s(pin:%d)" % (
          fm.str_function(function), pin_used)
      if force == False:
        raise Exception(info)
      else:
        print(info)
    __class__.fpioa.set_function(self, function)

  def unregister(self):
    __class__.fpioa.set_function(self, fm.fpioa.RESV0)

  def str_function(self):
    if fm.fpioa.GPIOHS0 <= self <= fm.fpioa.GPIO7:
      if fm.fpioa.GPIO0 <= self:
        return 'fm.fpioa.GPIO%d' % (self - fm.fpioa.GPIO0)
      return 'fm.fpioa.GPIOHS%d' % (self - fm.fpioa.GPIOHS0)
    return 'unknown'

  def get_gpio_used():
    return [(__class__.str_function(f), __class__.get_pin_by_function(f)) for f in range(fm.fpioa.GPIOHS0, fm.fpioa.GPIO7 + 1)]
