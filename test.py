from manimlib.imports import *

class Intro(Scene):

    def construct(self):
        over_title = TextMobject("The Eight Axioms")
        under_title = TextMobject("of Vector Spaces")
        under_title.next_to(over_title, DOWN)
        title = VGroup(over_title, under_title)

        self.wait(2)
        self.play(FadeIn(over_title))
        self.wait(1)
        self.play(Write(under_title, run_time = 2))
        self.wait(2)
        self.play(FadeOut(title))

class Definition(Scene):

    def construct(self):
        line1 = TexMobject("\\text{A set of vectors }", "V", """\\text{ is a
                           vector space over the field }""", "F",
                           "\\text{ if the operations")
        line1.set_color_by_tex_to_color_map({"V" : YELLOW, "F" : BLUE})
        operation1 = TexMobject("+ :", "V", "\\times", "V", "\\to", "V")
        operation1.set_color_by_tex_to_color_map({"V" : YELLOW})
        operation2 = TexMobject("\\cdot :", "F", "\\times", "V",  "\\to", "V")
        operation2.set_color_by_tex_to_color_map({"V" : YELLOW, "F" : BLUE})
        line2 = TexMobject("\\text{on }", "\\mathbf{x,y,z}",
                           "\\text{ and }", "a,b",
                            "\\text{ adhere to the axioms:}")
        line2.set_color_by_tex_to_color_map({ "\\mathbf{x,y,z}" : YELLOW,
                                             "a,b" : BLUE})

        ax1 = TexMobject("\\text{1. }", "\\mathbf{x}", "+ (", "\\mathbf{y}",
                         "+", "\\mathbf{z}", ") = (", "\\mathbf{x}", "+",
                         "\\mathbf{y}", ") +", "\\mathbf{z}")
        ax1.set_color_by_tex_to_color_map({"\\mathbf{x}" : YELLOW,
                                           "\\mathbf{y}" : YELLOW,
                                           "\\mathbf{z}" : YELLOW})
        ax2 = TexMobject("\\text{2. }", "\\mathbf{x}", "+", "\\mathbf{y}",
                         "=", "\\mathbf{y}", "+", "\\mathbf{x}")
        ax2.set_color_by_tex_to_color_map({"\\mathbf{x}" : YELLOW,
                                           "\\mathbf{y}" : YELLOW})
        ax3 = TexMobject("\\text{3. }", "\\exists \\mathbf{0} \\in", "V",
                         ":", "\\mathbf{x}", "+ \\mathbf{0} =", "\\mathbf{x}")
        ax3.set_color_by_tex_to_color_map({"\\mathbf{x}" : YELLOW,
                                           "V" : YELLOW})
        ax4 = TexMobject("\\text{4. }", "\\forall", "\\mathbf{x}", "\\in", "V",
                         ", \\exists", "\\mathbf{y}", "\\in",
                         "V", ":", "\\mathbf{x}",
                         "+", "\\mathbf{y}", "= \\mathbf{0}")
        ax4.set_color_by_tex_to_color_map({"\\mathbf{x}" : YELLOW,
                                           "\\mathbf{y}" : YELLOW,
                                           "V" : YELLOW})
        ax5 = TexMobject("\\text{5. }", "a", "(", "b", "\\mathbf{", "x}",
                         ") =", "(", "a", "b", ")", "\\mathbf{", "x}")
        ax5.set_color_by_tex_to_color_map({"x}" : YELLOW,
                                           "a" : BLUE, "b" : BLUE})
        ax6 = TexMobject("\\text{6. }", "1", "\\cdot", "\mathbf{", "x}",
                         "=", "\mathbf{", "x}")
        ax6.set_color_by_tex_to_color_map({"x}" : YELLOW,
                                           "1" : BLUE})
        ax7 = TexMobject("\\text{7. }", "a", "(", "\\mathbf{", "x}", "+",
                         "\\mathbf{", "y}", ") =", "a", "\\mathbf{", "x}",
                         "+", "a", "\\mathbf{", "y}")
        ax7.set_color_by_tex_to_color_map({"x}" : YELLOW,
                                           "y}" : YELLOW,
                                           "a" : BLUE})
        ax8 = TexMobject("\\text{8. }", "(", "a", "+", "b", ")", "\mathbf{",
                         "x}", "=", "a", "\\mathbf{", "x}", "+", "b",
                         "\\mathbf{", "x}")
        ax8.set_color_by_tex_to_color_map({"x}" : YELLOW,
                                           "a" : BLUE, "b" : BLUE})

        definition = VGroup(line1, operation1, operation2, line2)
        definition.arrange_submobjects(DOWN)
        definition.scale(0.75)

        ax2.align_to(ax1, LEFT)
        ax3.align_to(ax2, LEFT)
        ax4.align_to(ax3, LEFT)
        ax6.align_to(ax5, LEFT)
        ax7.align_to(ax6, LEFT)
        ax8.align_to(ax7, LEFT)
        ax1to4 = VGroup(ax1, ax2, ax3, ax4)
        ax5to8 = VGroup(ax5, ax6, ax7, ax8)

        for i, axiom in enumerate(ax1to4[1:], 1):
            axiom.shift(i*DOWN)
        for i, axiom in enumerate(ax5to8[1:], 1):
            axiom.shift(i*DOWN)

        axioms = VGroup(ax1to4, ax5to8)
        axioms.arrange_submobjects(RIGHT, buff = LARGE_BUFF)
        axioms.scale(0.75)


        self.play(Write(definition[0], run_time = 4))
        self.play(FadeIn(definition[1], run_time = 1))
        self.wait(1)
        self.play(FadeIn(definition[2], run_time = 1))
        self.wait(1)
        self.play(Write(definition[3], run_time = 2))
        self.add(definition)
        self.wait(2)
        self.play(ApplyMethod(definition.shift,3*UP))
        self.play(FadeIn(axioms[0]))
        self.play(FadeIn(axioms[1]))
        self.wait(3)
        self.play(FadeOut(definition))
        self.play(ApplyMethod(ax1.to_corner, UL))
        self.play(FadeOut(axioms[0][1:4]))
        self.play(FadeOut(axioms[1]))
        self.wait(3)

class Axiom1(Scene):

    def construct(self):
        ax1 = TexMobject("\\text{1. }", "\\mathbf{x}", "+ (", "\\mathbf{y}",
                         "+", "\\mathbf{z}", ") = (", "\\mathbf{x}", "+",
                         "\\mathbf{y}", ") +", "\\mathbf{z}")
        ax1.set_color_by_tex_to_color_map({"\\mathbf{x}" : YELLOW,
                                           "\\mathbf{y}" : YELLOW,
                                           "\\mathbf{z}" : YELLOW})
        ax1.scale(0.75)
        ax1.to_corner(UL)
        ax1_color = ax1.copy().set_color_by_tex_to_color_map({
                                        "\\mathbf{x}" : GREEN,
                                        "\\mathbf{y}" : RED,
                                        "\\mathbf{z}" : PURPLE})


        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([2, 2])
        y = Vector([2, -1])
        z = Vector([-1, -2])
        x_plus_y = Vector([4, 1])
        y_plus_z = Vector([1, -3])
        xyz = Vector([3, -1])
        x.set_color(GREEN)
        y.set_color(RED)
        z.set_color(PURPLE)
        x_plus_y.set_color(YELLOW)
        y_plus_z.set_color(YELLOW)
        xyz.set_color(GOLD_E)

        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        y_label = TexMobject("\\mathbf{y}").set_color(RED).next_to(2*RIGHT+DOWN, DOWN).scale(0.75)
        z_label = TexMobject("\\mathbf{z}").set_color(PURPLE).next_to(LEFT+2*DOWN, DOWN).scale(0.75)
        yplusz_label = TexMobject("(", "\\mathbf{y}", "+", "\\mathbf{z}", ")").scale(0.75)
        yplusz_label.next_to(RIGHT+3*DOWN, DOWN)
        xplusy_label = TexMobject("(", "\\mathbf{x}", "+", "\\mathbf{y}", ")").scale(0.75)
        xplusy_label.next_to(4*RIGHT+UP, RIGHT)
        yz_x_label = TexMobject("\\mathbf{x}", "+", "(", "\\mathbf{y}", "+", "\\mathbf{z}", ")").scale(0.75)
        yz_x_label.next_to(3*RIGHT+DOWN, RIGHT)
        xy_z_label = TexMobject("(", "\\mathbf{x}", "+", "\\mathbf{y}", ")", "+", "\\mathbf{z}").scale(0.75)
        xy_z_label.next_to(3*RIGHT+DOWN, RIGHT)
        yplusz_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                    "\\mathbf{z}" : PURPLE})
        xplusy_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                    "\\mathbf{x}" : GREEN})
        yz_x_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                  "\\mathbf{x}" : GREEN,
                                                  "\\mathbf{z}" : PURPLE})
        xy_z_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                  "\\mathbf{z}" : PURPLE,
                                                  "\\mathbf{x}" : GREEN})

        x_to_y = DashedLine(2*RIGHT+2*UP, 4*RIGHT+UP)
        y_to_x = DashedLine(2*RIGHT+DOWN, 4*RIGHT+UP)
        y_to_z = DashedLine(2*RIGHT+DOWN, RIGHT+3*DOWN)
        z_to_y = DashedLine(LEFT+2*DOWN, RIGHT+3*DOWN)
        xy_to_z = DashedLine(4*RIGHT+UP, 3*RIGHT+DOWN)
        z_to_xy = DashedLine(LEFT+2*DOWN, 3*RIGHT+DOWN)
        zy_to_x = DashedLine(RIGHT+3*DOWN, 3*RIGHT+DOWN)
        x_to_zy = DashedLine(2*RIGHT+2*UP, 3*RIGHT+DOWN)

        labels = VGroup(x_label, y_label, z_label)
        vectors = VGroup(x, y, z)
        sumvectors = VGroup(x_plus_y, y_plus_z)
        sumlabels = VGroup(yplusz_label, xplusy_label)
        sumyz = VGroup(y_plus_z, yplusz_label)
        sumxy = VGroup(x_plus_y, xplusy_label)
        xvec = VGroup(x, x_label)
        yvec = VGroup(y, y_label)
        zvec = VGroup(z, z_label)
        xyzvec = VGroup(xyz, yz_x_label)
        vectors_labeled = VGroup(xvec, yvec, zvec)

        lello1 = VGroup(y_to_z, z_to_y)
        lello2 = VGroup(x_to_y, y_to_x)
        lello3 = VGroup(xy_to_z, z_to_xy)
        lello4 = VGroup(zy_to_x, x_to_zy)

        self.add(ax1)
        self.play(ShowCreation(x_axis))
        self.play(ShowCreation(y_axis))
        self.play(ShowCreation(x_tick_marks))
        self.play(ShowCreation(y_tick_marks))
        self.play(Transform(ax1, ax1_color))
        self.play(ShowCreation(vectors), run_time = 2)
        self.play(Write(labels))
        self.add(vectors_labeled)
        self.remove(vectors)
        self.remove(labels)
        self.play(ShowCreation(lello1, run_time = 2))
        self.play(ShowCreation(y_plus_z))
        self.play(Write(yplusz_label))
        self.play(FadeOut(lello1))
        self.play(FadeOut(vectors_labeled[2]))
        self.play(FadeOut(vectors_labeled[1]))
        self.play(ShowCreation(lello4, run_time = 2))
        self.play(ShowCreation(xyz))
        self.play(Write(yz_x_label))
        self.play(FadeOut(lello4))
        self.play(FadeOut(sumyz))
        self.play(FadeOut(vectors_labeled[0]))
        self.play(FadeIn(vectors_labeled))
        self.play(ShowCreation(lello2, run_time = 2))
        self.play(ShowCreation(x_plus_y))
        self.play(Write(xplusy_label))
        self.play(FadeOut(lello2))
        self.play(FadeOut(vectors_labeled[0]))
        self.play(FadeOut(vectors_labeled[1]))
        self.play(ShowCreation(lello3, run_time = 2))
        self.wait(1)
        self.play(Transform(yz_x_label, xy_z_label))
        self.play(FadeOut(lello3))
        self.play(FadeOut(sumxy))
        self.play(FadeOut(vectors_labeled[2]))
        self.wait(2)
        self.play(FadeOut(xyzvec))
        self.wait(2)

class Axiom2(Scene):

    def construct(self):
        ax1 = TexMobject("\\text{1. }", "\\mathbf{x}", "+ (", "\\mathbf{y}",
                         "+", "\\mathbf{z}", ") = (", "\\mathbf{x}", "+",
                         "\\mathbf{y}", ") +", "\\mathbf{z}")
        ax1.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                        "\\mathbf{y}" : RED,
                                        "\\mathbf{z}" : PURPLE})

        ax2 = TexMobject("\\text{2. }", "\\mathbf{x}", "+", "\\mathbf{y}",
                         "=", "\\mathbf{y}", "+", "\\mathbf{x}")
        ax2.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                           "\\mathbf{y}" : RED})

        xplusy_label = TexMobject("(", "\\mathbf{x}", "+", "\\mathbf{y}", ")").scale(0.75)
        xplusy_label.next_to(4*RIGHT+UP, RIGHT)
        xplusy_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                    "\\mathbf{x}" : GREEN})
        yplusx_label = TexMobject("(", "\\mathbf{y}", "+", "\\mathbf{x}", ")").scale(0.75)
        yplusx_label.next_to(4*RIGHT+UP, RIGHT)
        yplusx_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                    "\\mathbf{x}" : GREEN})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        y_label = TexMobject("\\mathbf{y}").set_color(RED).next_to(2*RIGHT+DOWN, DOWN).scale(0.75)

        ax1.scale(0.75)
        ax2.scale(0.75)
        ax1.to_corner(UL)
        ax2.to_corner(UL)

        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([2, 2])
        y = Vector([2, -1])
        x_plus_y = Vector([4, 1])
        x.set_color(GREEN)
        y.set_color(RED)
        x_plus_y.set_color(YELLOW)
        xvec = VGroup(x, x_label)
        yvec = VGroup(y, y_label)
        vectors = VGroup(xvec, yvec)

        x_to_y = DashedLine(2*RIGHT+2*UP, 4*RIGHT+UP)
        y_to_x = DashedLine(2*RIGHT+DOWN, 4*RIGHT+UP)
        sumxy = VGroup(x_plus_y, xplusy_label)
        lello2 = VGroup(x_to_y, y_to_x)

        self.add(ax1)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax1, ax2))
        self.wait()
        self.play(ShowCreation(vectors), run_time = 2)
        self.play(ShowCreation(lello2), run_time = 2)
        self.play(ShowCreation(x_plus_y))
        self.play(ShowCreation(xplusy_label))
        self.play(Transform(xplusy_label, yplusx_label))
        self.wait(2)
        self.play(FadeOut(lello2))
        self.play(FadeOut(vectors))
        self.play(FadeOut(sumxy))
        self.wait(2)

class Axiom3(Scene):

    def construct(self):
        ax2 = TexMobject("\\text{2. }", "\\mathbf{x}", "+", "\\mathbf{y}",
                         "=", "\\mathbf{y}", "+", "\\mathbf{x}")
        ax2.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                           "\\mathbf{y}" : RED})
        ax3 = TexMobject("\\text{3. }", "\\exists \\mathbf{0} \\in", "V",
                         ":", "\\mathbf{x}", "+ \\mathbf{0} =", "\\mathbf{x}")
        ax3.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                           "V" : YELLOW})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        xplus0_label = TexMobject("\\mathbf{x}", "+", "\\mathbf{0}").scale(0.75)
        xplus0_label.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN}).next_to(2*RIGHT+2*UP, RIGHT)


        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([2, 2])
        x.set_color(GREEN)
        origin = Dot(radius = 0.1).set_color(WHITE)
        origin_label = TexMobject("\\mathbf{0}").scale(0.75)
        origin_label.next_to(origin, RIGHT+DOWN)
        zerovec = VGroup(origin, origin_label)
        xvec = VGroup(x, x_label)

        ax2.scale(0.75)
        ax3.scale(0.75)
        ax2.to_corner(UL)
        ax3.to_corner(UL)

        self.add(ax2)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax2, ax3))
        self.wait(2)
        self.play(ShowCreation(xvec))
        self.play(ShowCreation(zerovec))
        self.play(ApplyMethod(zerovec.shift, 2*RIGHT+2*UP), run_time = 2)
        self.play(FadeOut(zerovec))
        self.play(Transform(x_label, xplus0_label))
        self.wait(2)
        self.play(FadeOut(xvec))
        self.wait(2)

class Axiom4(Scene):

    def construct(self):
        ax3 = TexMobject("\\text{3. }", "\\exists \\mathbf{0} \\in", "V",
                         ":", "\\mathbf{x}", "+ \\mathbf{0} =", "\\mathbf{x}")
        ax3.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                           "V" : YELLOW})
        ax4 = TexMobject("\\text{4. }", "\\forall", "\\mathbf{x}", "\\in", "V",
                         ", \\exists", "\\mathbf{y}", "\\in",
                         "V", ":", "\\mathbf{x}",
                         "+", "\\mathbf{y}", "= \\mathbf{0}")
        ax4.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                           "\\mathbf{y}" : RED,
                                           "V" : YELLOW})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        y_label = TexMobject("\\mathbf{y}").set_color(RED).next_to(2*LEFT+2*DOWN, DOWN).scale(0.75)
        xplusy_label = TexMobject("\\mathbf{x}", "+", "\\mathbf{y}").scale(0.75)
        xplusy_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                    "\\mathbf{x}" : GREEN})

        ax3.scale(0.75)
        ax4.scale(0.75)
        ax3.to_corner(UL)
        ax4.to_corner(UL)

        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([2, 2])
        x.set_color(GREEN)
        xvec = VGroup(x, x_label)
        y = Vector([-2, -2])
        y.set_color(RED)
        yvec = VGroup(y, y_label)
        origin = Dot(radius = 0.1).set_color(WHITE)
        origin_label = TexMobject("\\mathbf{0}")
        origin_label.next_to(origin, RIGHT+DOWN)
        zerovec = VGroup(origin, origin_label)
        xy = VGroup(xvec, yvec)
        xplusy_label.next_to(origin, RIGHT+DOWN)

        self.add(ax3)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax3, ax4))
        self.wait(2)
        self.play(ShowCreation(xvec))
        self.play(ShowCreation(yvec))
        self.play(ShowCreation(zerovec))
        self.wait(2)
        self.play(Transform(xy, origin))
        self.play(Transform(origin_label, xplusy_label))
        self.wait(3)

class Axiom5(Scene):

    def construct(self):
        ax4 = TexMobject("\\text{4. }", "\\forall", "\\mathbf{x}", "\\in", "V",
                         ", \\exists", "\\mathbf{y}", "\\in",
                         "V", ":", "\\mathbf{x}",
                         "+", "\\mathbf{y}", "= \\mathbf{0}")
        ax4.set_color_by_tex_to_color_map({"\\mathbf{x}" : GREEN,
                                           "\\mathbf{y}" : RED,
                                           "V" : YELLOW})
        ax5 = TexMobject("\\text{5. }", "a", "(", "b", "\\mathbf{", "x}",
                         ") =", "(", "a", "b", ")", "\\mathbf{", "x}")
        ax5.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "a" : BLUE, "b" : BLUE})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(RIGHT+UP, RIGHT).scale(0.75)
        a = TexMobject("a").set_color(BLUE).scale(0.75)
        b = TexMobject("b").set_color(BLUE).scale(0.75)
        bx_label = TexMobject("(", "b", "\\mathbf{", "x}", ")").next_to(x_label).scale(0.75)
        bx_label.set_color_by_tex_to_color_map({"x}" : GREEN,
                                                "b" : BLUE})
        abx_label = TexMobject("a", "(", "b", "\\mathbf{", "x}", ")").scale(0.75)
        abx_label.set_color_by_tex_to_color_map({"x}" : GREEN,
                                                "a" : BLUE,
                                                 "b" : BLUE})
        abx2_label = TexMobject("(", "a", "b", ")", "\\mathbf{", "x}").scale(0.75)
        abx2_label.set_color_by_tex_to_color_map({"x}" : GREEN,
                                                "a" : BLUE,
                                                 "b" : BLUE})


        ax4.scale(0.75)
        ax5.scale(0.75)
        ax4.to_corner(UL)
        ax5.to_corner(UL)

        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([1, 1])
        x.set_color(GREEN)
        xvec = VGroup(x, x_label)
        bx = Vector([2, 2]).set_color(GREEN)
        bxvec = VGroup(bx, bx_label)
        abx = Vector([3, 3]).set_color(GREEN)
        point = Dot(3*RIGHT+3*UP)
        x2 = x.copy()
        x_label2 = x_label.copy()
        xvec2 = VGroup(x2, x_label2)
        abx_label.next_to(point, RIGHT)
        abx2_label.next_to(point, RIGHT)
        abxvec1 = VGroup(abx, point, abx_label)

        self.add(ax4)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax4, ax5))
        self.wait(2)
        self.play(ShowCreation(xvec))
        self.wait()
        self.play(Transform(xvec, bxvec))
        self.wait()
        self.play(Transform(xvec, abxvec1))
        self.add(point)
        self.add(abx_label)
        self.wait()
        self.play(FadeOut(xvec))
        self.wait(2)
        self.play(ShowCreation(xvec2))
        self.wait()
        self.remove(x_label2)
        self.play(Transform(x2, abx))
        self.play(Transform(abx_label, abx2_label))
        self.play(FadeOut(point))
        self.wait(2)
        self.play(FadeOut(abx_label))
        self.play(FadeOut(x2))
        self.wait(2)

class Axiom6(Scene):

    def construct(self):
        ax5 = TexMobject("\\text{5. }", "a", "(", "b", "\\mathbf{", "x}",
                         ") =", "(", "a", "b", ")", "\\mathbf{", "x}")
        ax5.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "a" : BLUE, "b" : BLUE})
        ax6 = TexMobject("\\text{6. }", "1", "\\cdot", "\mathbf{", "x}",
                         "=", "\mathbf{", "x}")
        ax6.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "1" : BLUE})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        one = TexMobject("1", "\\cdot", "\\mathbf{", "x}").next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        one.set_color_by_tex_to_color_map({"1" : BLUE, "x}" : GREEN})

        ax5.scale(0.75)
        ax6.scale(0.75)
        ax5.to_corner(UL)
        ax6.to_corner(UL)

        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([2, 2])
        x.set_color(GREEN)
        xvec = VGroup(x, x_label)

        self.add(ax5)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax5, ax6))
        self.wait(2)
        self.play(ShowCreation(xvec))
        self.wait()
        self.play(Transform(x_label, one))
        self.wait()
        self.play(FadeOut(xvec))
        self.wait(2)

class Axiom7(Scene):

    def construct(self):
        ax6 = TexMobject("\\text{6. }", "1", "\\cdot", "\mathbf{", "x}",
                         "=", "\mathbf{", "x}")
        ax6.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "1" : BLUE})
        ax7 = TexMobject("\\text{7. }", "a", "(", "\\mathbf{", "x}", "+",
                         "\\mathbf{", "y}", ") =", "a", "\\mathbf{", "x}",
                         "+", "a", "\\mathbf{", "y}")
        ax7.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "y}" : RED,
                                           "a" : BLUE})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).next_to(2*RIGHT+2*UP, RIGHT).scale(0.75)
        y_label = TexMobject("\\mathbf{y}").set_color(RED).next_to(2*RIGHT+DOWN, DOWN).scale(0.75)
        xplusy_label = TexMobject("(", "\\mathbf{x}", "+", "\\mathbf{y}", ")").scale(0.75)
        xplusy_label.next_to(4*RIGHT+UP, DOWN)
        xplusy_label.set_color_by_tex_to_color_map({"\\mathbf{y}" : RED,
                                                    "\\mathbf{x}" : GREEN})
        ax_label = TexMobject("a", "\\mathbf{x}").next_to(3*RIGHT+3*UP).scale(0.75)
        ax_label.set_color_by_tex_to_color_map({"a" : BLUE, "\\mathbf{x}" : GREEN})
        ay_label = TexMobject("a", "\\mathbf{y}").next_to(3*RIGHT+1.5*DOWN).scale(0.75)
        ay_label.set_color_by_tex_to_color_map({"a" : BLUE, "\\mathbf{y}" : RED})
        axy_label = TexMobject("a", "(", "\\mathbf{x}", "+", "\\mathbf{y}", ")").scale(0.75)
        axy_label.next_to(6*RIGHT+1.5*UP, UP)
        axy_label.set_color_by_tex_to_color_map({"a" : BLUE, "\\mathbf{x}" : GREEN, "\\mathbf{y}" : RED})
        ax_plus_ay_label = TexMobject("a", "\\mathbf{x}", "+", "a",
                                      "\\mathbf{y}").next_to(6*RIGHT+1.5*UP, UP).scale(0.75)
        ax_plus_ay_label.set_color_by_tex_to_color_map({"a" : BLUE, "\\mathbf{y}" : RED,
                                                 "\\mathbf{x}" : GREEN})

        ax6.scale(0.75)
        ax7.scale(0.75)
        ax6.to_corner(UL)
        ax7.to_corner(UL)

        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([2, 2])
        y = Vector([2, -1])
        x_plus_y = Vector([4, 1])
        ax = Vector([3, 3])
        ay = Vector([3, -1.5])
        ax_plus_ay = Vector([6, 1.5])
        x.set_color(GREEN)
        y.set_color(RED)
        ax.set_color(GREEN)
        ay.set_color(RED)
        x_plus_y.set_color(YELLOW)
        ax_plus_ay.set_color(YELLOW)
        xvec = VGroup(x, x_label)
        yvec = VGroup(y, y_label)
        vectors = VGroup(xvec, yvec)
        vectors = VGroup(x, y)
        sumxy = VGroup(x_plus_y, xplusy_label)
        xvec = VGroup(x, x_label)
        yvec = VGroup(y, y_label)
        axvec = VGroup(ax, ax_label)
        ayvec = VGroup(ay, ay_label)
        vectors_labeled = VGroup(xvec, yvec)

        x_to_y = DashedLine(2*RIGHT+2*UP, 4*RIGHT+UP)
        y_to_x = DashedLine(2*RIGHT+DOWN, 4*RIGHT+UP)
        ax_to_ay = DashedLine(3*RIGHT+3*UP, 6*RIGHT+1.5*UP)
        ay_to_ax = DashedLine(3*RIGHT+1.5*DOWN, 6*RIGHT+1.5*UP)

        labels = VGroup(x_label, y_label)
        lello2 = VGroup(x_to_y, y_to_x)
        lello5 = VGroup(ax_to_ay, ay_to_ax)
        sumxy = VGroup(x_plus_y, xplusy_label)
        avecs = VGroup(axvec, ayvec)

        self.add(ax6)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax6, ax7))
        self.wait(2)
        self.play(ShowCreation(vectors_labeled))
        self.wait()
        self.play(ShowCreation(lello2))
        self.play(ShowCreation(sumxy), run_time = 2)
        self.play(FadeOut(lello2))
        self.play(FadeOut(vectors_labeled))
        self.play(Transform(sumxy[0], ax_plus_ay))
        self.play(Transform(sumxy[1], axy_label))
        self.wait(2)
        self.play(ShowCreation(axvec))
        self.play(ShowCreation(ayvec))
        self.wait()
        self.play(ShowCreation(lello5), run_time = 2)
        self.wait()
        self.play(Transform(sumxy[1], ax_plus_ay_label))
        self.play(FadeOut(lello5))
        self.play(FadeOut(avecs))
        self.play(FadeOut(sumxy[1]))
        self.play(FadeOut(sumxy[0]))
        self.wait(2)

class Axiom8(Scene):

    def construct(self):
        ax7 = TexMobject("\\text{7. }", "a", "(", "\\mathbf{", "x}", "+",
                         "\\mathbf{", "y}", ") =", "a", "\\mathbf{", "x}",
                         "+", "a", "\\mathbf{", "y}")
        ax7.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "y}" : RED,
                                           "a" : BLUE})
        ax8 = TexMobject("\\text{8. }", "(", "a", "+", "b", ")", "\mathbf{",
                         "x}", "=", "a", "\\mathbf{", "x}", "+", "b",
                         "\\mathbf{", "x}")
        ax8.set_color_by_tex_to_color_map({"x}" : GREEN,
                                           "a" : BLUE, "b" : BLUE})
        x_label = TexMobject("\\mathbf{x}").set_color(GREEN).scale(0.75).next_to(0.5*RIGHT+0.5*UP)
        ax_label = TexMobject("a", "\\mathbf{x}").scale(0.75)
        ax_label.next_to(RIGHT+UP)
        ax_label.set_color_by_tex_to_color_map({"a" : BLUE, "\\mathbf{x}" : GREEN})
        bx_label = TexMobject("b", "\\mathbf{x}").scale(0.75)
        bx_label.next_to(2*RIGHT+2*UP)
        bx_label.set_color_by_tex_to_color_map({"b" : BLUE, "\\mathbf{x}" : GREEN})
        axbx_label = TexMobject("a", "\\mathbf{x}", "+", "b", "\\mathbf{x}").scale(0.75)
        axbx_label.next_to(3*RIGHT+3*UP)
        axbx_label.set_color_by_tex_to_color_map({"a" : BLUE, "b" : BLUE, "\\mathbf{x}" : GREEN})
        abx_label = TexMobject("(", "a", "+", "b", ")", "\\mathbf{x}").scale(0.75)
        abx_label.next_to(3*RIGHT+3*UP)
        abx_label.set_color_by_tex_to_color_map({"a" : BLUE, "b" : BLUE, "\\mathbf{x}" : GREEN})

        ax7.scale(0.75)
        ax8.scale(0.75)
        ax7.to_corner(UL)
        ax8.to_corner(UL)

        plane = NumberPlane()
        x_axis, y_axis = plane.get_axes().copy().split()
        number_line = NumberLine(tick_frequency = 1)
        x_tick_marks = number_line.get_tick_marks()
        x_tick_marks.set_color(WHITE)
        y_tick_marks = x_tick_marks.copy().rotate(np.pi/2)

        x = Vector([0.5, 0.5])
        x.set_color(GREEN)
        xvec = VGroup(x, x_label)
        ax = Vector([1, 1])
        ax.set_color(GREEN)
        axvec = VGroup(ax, ax_label)
        bx = Vector([2, 2])
        bx.set_color(GREEN)
        bxvec = VGroup(bx, bx_label)
        axbx = Vector([3, 3])
        axbx.set_color(GREEN)
        axbxvec = VGroup(axbx, axbx_label)
        point = Dot(3*RIGHT+3*UP)
        x2 = x.copy()
        x2_label = x_label.copy()
        xvec2 = VGroup(x2, x2_label)
        axbx_label2 = axbx_label.copy()

        self.add(ax7)
        self.add(x_axis)
        self.add(y_axis)
        self.add(x_tick_marks)
        self.add(y_tick_marks)
        self.play(Transform(ax7, ax8))
        self.wait(2)
        self.play(ShowCreation(xvec))
        self.wait()
        self.play(Transform(xvec, axvec))
        self.wait()
        self.play(ShowCreation(bxvec))
        self.wait()
        self.play(ApplyMethod(xvec.shift,2*RIGHT+2*UP))
        self.wait()
        self.play(ShowCreation(point))
        self.play(ShowCreation(axbx_label2))
        self.play(FadeOut(bxvec))
        self.play(FadeOut(xvec))
        self.wait()
        self.play(ShowCreation(axbx))
        self.wait()
        self.play(Transform(axbx_label2, abx_label))
        self.play(FadeOut(point))
        self.play(FadeOut(axbx))
        self.play(FadeOut(axbx_label2))
        self.play(FadeOut(ax7))
        self.play(FadeOut(x_tick_marks))
        self.play(FadeOut(y_tick_marks))
        self.play(FadeOut(x_axis))
        self.play(FadeOut(y_axis))
        self.wait(2)




