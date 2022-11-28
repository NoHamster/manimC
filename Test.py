from manim import *


class Iterate(Animation):
    def __init__(self, mobject, start=0, **kwargs):
        super.__init__(mobject, **kwargs)
        self.pos=start

    def begin(self):
        self.elements=self.mobject.get_entries()

        e = self.elements[pos]
        rect = SurroundingRectangle(e)
        self.add(rect)
        while(pos<len(self.elements)):
            self.play(rect.move_to(e))
            yield e

        self.remove(rect)


class List(Matrix):


    CONFIG = {
        "element_to_mobject" : Text,
    }
    def __init__(self, elements, **kwargs):
        kwargs["left_bracket"] = "\\{"
        kwargs["right_bracket"] = "\\}"
        if "h_buff" in kwargs:
            kwargs["h_buff"] +=0.5
        Matrix.__init__(self, [elements], **kwargs)

        self.add_comma()

    def add_comma(self):
        self.commas = []
        for e in self.get_entries()[:-1]:
            tmp = Text(",")
            tmp.next_to(e, RIGHT, 0.125)
            tmp.shift(DOWN*0.25)
            self.add(tmp)
            self.commas.append(tmp)
        return self

class Test(Scene):
    def construct(self):
        m0 = List(range(10))
        self.add(m0)
        for i in m0.iter():
            print(i)
        self.play(FadeOut(m0))

