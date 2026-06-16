# and , or, not
# > 35 pass,  < 35 fail

maths = 45
science = 32
english = 50

print(maths > 35 and science > 35 and english > 35)

print(maths > 35 or science > 35 or english > 35)

print(maths > 35 and science > 35 or english > 35)

print(maths > 35 and not science > 35 and english > 35)

print(not(maths > 35 and not science > 35 and english > 35))
