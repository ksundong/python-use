class MyClass(object):
    def method_a(self):
        # 인터페이스만 구현할 때 많이 사용
        pass  # 그냥 빈 라인을 넣으면 오류가 발생한다.

    def method_b(self):
        print("Method B")


c = MyClass()
