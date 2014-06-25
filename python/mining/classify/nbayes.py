#!/usr/bin/env python
# coding: utf8


class Bayes(object):
    def __init__(self, storage, prefix="bayes"):
        self.storage = storage
        self.prefix = prefix

    def learn(self, cls, words):
        for word in words:
            self.storage.incr("%s:%s:%s" % (self.prefix, cls, word.__hash__()))
        self.storage.incr("%s:%s" % (self.prefix, cls))

    def classify(self, cls, words):
        laplace_cnt = 0
        cls_word_cnts = []
        for word in words:
            value = self.storage.get("%s:%s:%s" % (self.prefix, cls, word.__hash__()))
            if value:
                cls_word_cnts.append(int(value))
            else:
                laplace_cnt += 1
                cls_word_cnts.append(1)
        cls_cnt = int(self.storage.get("%s:%s" % (self.prefix, cls)) or 0) + laplace_cnt

        if cls_cnt == 0:
            return 0

        p_word_cls = [(float(cnt) / cls_cnt) for cnt in cls_word_cnts]
        p_cls = 1
        for p_word in p_word_cls:
            p_cls *= p_word


        return p_cls


def show(clses, words):
    import redis
    conn = redis.StrictRedis()
    bayes = Bayes(conn)
    print "".join(words)
    for cls in clses:
        print cls, ":",
        print bayes.classify(cls, words)
    print ""


def test():
    """
    import redis
    conn = redis.StrictRedis()
    bayes = Bayes(conn)
    spam_corporas = [("A", "B"), ("B", "C")]
    normal_corporas = [("A", "C")]
    for corpora in spam_corporas:
        bayes.learn("spam", corpora)

    for corpora in normal_corporas:
        bayes.learn("normal", corpora)
    """

    show(("spam", "normal", "unknown"), ("A", "B"))
    show(("spam", "normal", "unknown"), ("B", "C"))
    show(("spam", "normal", "unknown"), ("A", "C"))
    show(("spam", "normal", "unknown"), ("A", "B", "C"))
    show(("spam", "normal", "unknown"), ("A", "B", "C", "D", "E", "F"))


if __name__ == "__main__":
    test()
