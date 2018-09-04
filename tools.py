class PageBar:
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    def __init__(self, page_num, page_total):
        self.page_total = page_total
        self.page_num = page_num
        if self.page_num <= 5:
            self.left = 1
            self.right = 10
            self.mode = PageBar.LEFT
        elif self.page_num >= self.page_total - 4:
            self.left = self.page_total - 9
            self.right = self.page_total
            self.mode = PageBar.RIGHT
        else:
            self.left = self.page_num - 5
            self.right = self.page_num + 4
            self.mode = PageBar.MIDDLE


