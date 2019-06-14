# 기본 인수값
def incr(a, step=1):
    return a + step

# 오류
# def decr(step=1, a):
#    return a + step


print(incr(10))
print(incr(10, step=2))
print(incr(10, 4))

#  키워드 인수
def area(width, height):
    return width * height

print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))
# 오류
#area(20, width=10)
#area(height=20, 10)

# 가변인수
def vargs(a, *args):
    print(a, args)


vargs(10)
vargs(10, 1)
vargs(10, 1, 2, 3, 4, 5)

def _print(*args, end='newline'):
    print(args, end)

_print(10, 20, 30)
_print(10, end='tab')
_print(10, 'tab')

