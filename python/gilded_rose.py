# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrease_quality(self, item, rate):
        '''
        The quality of an item is never negative
        '''
        item.quality -= rate
        if item.quality < 0:
            item.quality = 0

    def increase_quality(self, item, rate):
        '''
        The quality of an item except Sulfuras is never more than 50
        '''
        item.quality += rate
        if item.quality > 50:
            item.quality = 50

    def zero_quality(self, item):
        item.quality = 0

    def determine_rate(self, item):
        '''
        Determine the quality rate
        '''
        rate = 0
        if "Conjured" in item.name:
            rate = 2
        elif "Backstage passes" in item.name:
            if 5 < item.sell_in <= 10:
                rate = 2
            elif item.sell_in <= 5:
                rate = 3
            else:
                rate = 1
        else:
            if item.sell_in < 0:
                rate = 2
            else:
                rate = 1
        return rate
    
    def decrease_sell_in(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.sell_in = -1

    def update_quality(self):
        for item in self.items:
            rate = self.determine_rate(item)
            if item.name == "Aged Brie":
                self.increase_quality(item, rate)
            elif "Backstage passes" in item.name:
                if item.sell_in <= 0:
                    self.zero_quality(item)
                else:
                    self.increase_quality(item, rate)
            elif "Sulfuras" not in item.name:
                self.decrease_quality(item, rate)
            self.decrease_sell_in(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
