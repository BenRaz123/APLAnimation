from manim import *

BEN_BLUE = "#235ceb"
BEN_RED = "#e31010"
BEN_YELLOW = "#e3c310"

class MorphAnimation(Scene):
  def construct(self):
    title = Title(r"Python")
    title2 = Title(r"APL")
    code = 'chars = [...] \n for i in range(len(chars-1)): \n  sym = chars[randint(0,max)] \n  print(sym, end="")'
    apl = '“…”[16?73]'
    pythonCode = Code(language = "python", code=code, font="SF Mono", background="window", insert_line_no=False, line_spacing=0.5)
    aplCode = Code(language= "apl",code=apl, font="SF Mono", background="window", insert_line_no=False, line_spacing=0.5, font_size=48)
    self.play(FadeIn(pythonCode), Write(title))
    self.wait()
    self.play(ClockwiseTransform(pythonCode, aplCode), Transform(title, title2))
    self.wait()
class SecondAnimation(Scene):
  def construct(self):

    # Camera
    self.camera.background_color = BLACK

    # Background
    func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
   
    bgF = StreamLines(func, colors=[BEN_RED, BEN_BLUE], max_color_scheme_value=2).scale(1.2)
    bgC = Rectangle(color=BLACK, fill_opacity=0.9).scale(30)
    bgG = StreamLines(func, colors=[BEN_RED, BEN_BLUE], max_color_scheme_value=2, stroke_width=2000).scale(1.2)
    bgB = Rectangle(color=BLACK, fill_opacity=1).scale(30)

    bg = VGroup(bgB, bgG, bgC, bgF)

    bgF2 = StreamLines(func, colors=[BEN_YELLOW, DARKER_GRAY], max_color_scheme_value=2).scale(1.2)
    bgC2 = Rectangle(color=BLACK, fill_opacity=0.9).scale(30)
    bgG2 = StreamLines(func, colors=[BEN_YELLOW, DARKER_GRAY], max_color_scheme_value=2, stroke_width=2000).scale(1.2)
    bg2= VGroup(bgG2, bgC2, bgF2)


    self.add(bg2, bg)

    # Arr & APL Text & Positioning
    arr = Text('"..."', font= "SF Mono", color=BEN_BLUE)
    arrBrace = Brace(arr, DOWN, color =  BLACK)
    arrBraceText = arrBrace.get_text(f"Array").set_fill(BLACK)
    arrBraceG = VGroup(arrBrace, arrBraceText)

    # APL Text, Brace, & Positioning
    apl = Text("[16?73]", font = "SF Mono", color = BEN_RED)
    apl.next_to(arr, RIGHT)
    VGroup(arr, apl).center().scale(1.5)
    
    # Braces
    arrBrace = Brace(arr, DOWN, color =  WHITE)
    arrBraceText = arrBrace.get_text(f"Array").set_fill(WHITE).set_background_stroke(opacity=1, color=BLACK)
    arrBraceG = VGroup(arrBrace, arrBraceText)
    aplBrace = Brace(apl, UP, color = WHITE)
    aplBraceText = aplBrace.get_text(f"Extractive Randomized Function").set_fill(WHITE).set_background_stroke(opacity=1, color=BLACK)
    aplBraceG = VGroup(aplBrace, aplBraceText)

    # Result Text & Brace
    res = Tex("hkWrLQ4jso;6i7pv", color=BEN_YELLOW).scale(1.5)
    resBrace = Brace(res, UP, color = WHITE)
    resBraceText = resBrace.get_text(f"Result").set_fill(WHITE).set_background_stroke(opacity=1, color=BLACK)
    resBraceG = VGroup(resBrace, resBraceText)
    
    # Grouping
    a = VGroup(apl, arr)
    
    # Animations
    self.play(FadeIn(apl, shift= LEFT*2, scale = 0.5), FadeIn(arr, shift=RIGHT*2, scale=0.5))
    self.play(GrowFromCenter(aplBrace), FadeIn(aplBraceText, shift=UP , scale = 0.5), GrowFromCenter(arrBrace), FadeIn(arrBraceText, shift=DOWN , scale = 0.5))
    self.wait()
    self.play(FadeOut(arrBraceG, aplBraceG))
    self.play(FadeOut(bg), Transform(a, res))
    self.play(GrowFromCenter(resBrace), FadeIn(resBraceText, shift = UP , scale = 0.5))