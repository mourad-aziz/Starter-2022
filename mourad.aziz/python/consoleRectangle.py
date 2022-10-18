class ConsoleRectangle:

    def __init__(self, width, height, location, borderColor):
        #instance fields found by C# to Python Converter:
        self._hWidth = 0
        self._hHeight = 0
        self._hLocation = Point()
        self._hBorderColor = 0

        self._hWidth = width
        self._hHeight = height
        self._hLocation = location
        self._hBorderColor = borderColor

    def get_location(self):
        return self._hLocation
    def set_location(self, value):
        self._hLocation = value

    def get_width(self):
        return self._hWidth
    def set_width(self, value):
        self._hWidth = value

    def get_height(self):
        return self._hHeight
    def set_height(self, value):
        self._hHeight = value

    def get_border_color(self):
        return self._hBorderColor
    def set_border_color(self, value):
        self._hBorderColor = value

    def Draw(self):
        s = "╔"
        space = ""
        temp = ""
        i = 0
        while i < self.get_width():
            space += " "
            s += "═"
            i += 1

        j = 0
        while j < self.get_location().X:
            temp += " "
            j += 1

        s += "╗" + "\n"

        i = 0
        while i < self.get_height():
            s += temp + "║" + space + "║" + "\n"
            i += 1

        s += temp + "╚"
        i = 0
        while i < self.get_width():
            s += "═"
            i += 1

        s += "╝" + "\n"

        Console.ForegroundColor = self.get_border_color()
        Console.CursorTop = self._hLocation.Y
        Console.CursorLeft = self._hLocation.X
        print(s, end = '')
        Console.ResetColor()
