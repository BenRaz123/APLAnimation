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
    self.camera.background_color = WHITE

    # Array Text & Brace
    arr = Text('"..."', font= "SF Mono", color=BEN_BLUE)
    arrBrace = Brace(arr, DOWN, color =  BLACK)
    arrBraceText = arrBrace.get_text(f"Array").set_fill(BLACK)
    arrBraceG = VGroup(arrBrace, arrBraceText)

    # APL Text, Brace, & Positioning
    apl = Text("[16?73]", font = "SF Mono", color = BEN_RED)
    aplBrace = Brace(apl, UP, color = BLACK)
    aplBraceText = aplBrace.get_text(f"Extractive Randomized Function").set_fill(BLACK)
    aplBraceG = VGroup(aplBrace, aplBraceText)
    apl.next_to(arr, RIGHT)

    # Result Text & Brace
    res = Tex("hkWrLQ4jso;6i7pv", color=BEN_YELLOW).scale(1.5)
    resBrace = Brace(res, UP, color = BLACK)
    resBraceText = resBrace.get_text(f"Result").set_fill(BLACK)
    resBraceG = VGroup(resBrace, resBraceText)
    
    # Grouping
    VGroup(arr, apl).center().scale(1.5)
    a = VGroup(apl, arr)
    
    # Animations
    self.play(FadeIn(apl, shift= LEFT*2, scale = 0.5), FadeIn(arr, shift=RIGHT*2, scale=0.5))
    self.play(GrowFromCenter(aplBrace), FadeIn(aplBraceText, shift=UP , scale = 0.5), GrowFromCenter(arrBrace), FadeIn(arrBraceText, shift=DOWN , scale = 0.5))
    self.wait()
    self.play(FadeOut(arrBraceG, aplBraceG))
    self.play(Transform(a, res))
    self.play(GrowFromCenter(resBrace), FadeIn(resBraceText, shift = UP , scale = 0.5))