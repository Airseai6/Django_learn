# -*- coding: utf-8 -*-


class PageInfo(object):

    def __init__(self, current_page, all_count, per_page, base_url, show_page=11):
        """
        分页代码
        """
        try:
            self.current_page = int(current_page)
        except Exception as e:
            print(e)
            self.current_page = 1
        self.per_page = per_page

        a, b = divmod(all_count, per_page)
        if b:
            a += 1
        self.all_pager = a
        self.show_page = show_page
        self.base_url = base_url

    def start(self):
        return (self.current_page - 1)*self.per_page

    def end(self):
        return self.current_page*self.per_page

    def pager(self):

        page_list = []

        if self.all_pager < self.show_page:
            begin = 1
            stop = self.all_pager+1
        else:
            half = int((self.show_page-1)/2)
            if self.current_page <= half:
                begin = 1
                stop = self.show_page+1
            elif self.current_page >= self.all_pager - half:
                begin = self.all_pager - self.show_page + 1
                stop = self.all_pager+1
            else:
                begin = self.current_page - half
                stop = self.current_page + half + 1

        if self.current_page > 1:
            prev = "<li><a href='%s?page=%s'><<</a></li>" % (
                self.base_url, self.current_page - 1,)
            page_list.append(prev)

        for i in range(begin, stop):
            if i == self.current_page:
                temp = "<li class='active'><a href='%s?page=%s'>%s</a></li>" % (
                    self.base_url, i, i)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>" % (
                    self.base_url,  i, i)

            page_list.append(temp)

        if self.current_page < self.all_pager:
            nextpage = "<li><a href='%s?page=%s'>>></a></li>" % (
                self.base_url, self.current_page + 1,)
            page_list.append(nextpage)

        return ''.join(page_list)
