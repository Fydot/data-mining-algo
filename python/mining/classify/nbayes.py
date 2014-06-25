#!/usr/bin/env python
# coding: utf8


class Bayes(object):
    def __init__(self, storage, prefix="bayes"):
        self.storage = storage
        self.prefix = prefix

    def learn(self, cls, words):
        for word in words:
            if not self.storage.exists("%s:%s" % (self.prefix, word.__hash__())):
                self.storage.incr("%s:words" % self.prefix)
            self.storage.incr("%s:%s:%s" % (self.prefix, cls, word.__hash__()))
            self.storage.incr("%s:%s" % (self.prefix, word.__hash__()))
        self.storage.incr("%s:%s" % (self.prefix, cls))
        self.storage.incr("%s:record" % self.prefix)

    def classify(self, cls, words):
        length = int(self.storage.get("%s:words" % self.prefix)) if self.storage.get("%s:words" % self.prefix) else 0
        cls_word_cnt_power = 1
        word_cnt_power = 1
        for word in words:
            cls_word_cnt = self.storage.get("%s:%s:%s" % (self.prefix, cls, word.__hash__()))
            word_cnt = self.storage.get("%s:%s" % (self.prefix, word.__hash__()))

            cls_word_cnt_power *= int(cls_word_cnt) if cls_word_cnt else 0.000001
            word_cnt_power *= int(word_cnt) if word_cnt else 0.000001
        cls_cnt = self.storage.get("%s:%s" % (self.prefix, cls))
        cls_cnt_power = (int(cls_cnt) if cls_cnt else 0.000001) ** (length - 1)

        record_cnt = int(self.storage.get("%s:record" % self.prefix) or 0)

        return float(cls_word_cnt_power * (record_cnt ** (length - 1))) / (cls_cnt_power * word_cnt_power)


def test():
    import redis

    conn = redis.StrictRedis()

    bayes = Bayes(conn)

    """
    spam_corporas = [("A", "B"), ("B", "C")]
    normal_corporas = [("A", "C")]

    for corpora in spam_corporas:
        bayes.learn("spam", corpora)

    for corpora in normal_corporas:
        bayes.learn("normal", corpora)
    """

    print bayes.classify("spam", ("A", "B", "C"))
    print bayes.classify("spam", ("A", "B", "C", "D", "E", "F"))
    print bayes.classify("normal", ("A", "B", "C"))
    print bayes.classify("normal", ("A", "B", "C", "D", "E", "F"))


if __name__ == "__main__":
    test()
