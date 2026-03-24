# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    def update(self, item):
        raise NotImplementedError("Subclasses must implement update().")

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)


class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item, 1)


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        self.increase_quality(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.increase_quality(item, 1)


class BackstagePassUpdater(ItemUpdater):
    def _get_quality_increase(self, days_remaining):
        """Calculate quality increase based on days until concert.
        
        Args:
            days_remaining: Number of days until concert (sell_in value)
            
        Returns:
            Quality increase amount: 1 (>10 days), 2 (6-10 days), 3 (1-5 days), 0 (after concert)
        """
        if days_remaining < 6:
            return 3
        if days_remaining < 11:
            return 2
        return 1

    def update(self, item):
        quality_increase = self._get_quality_increase(item.sell_in)
        self.increase_quality(item, quality_increase)

        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class ConjuredUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 2)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item, 2)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def get_updater(self, item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        if item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        if item.name == "Conjured Mana Cake":
            return ConjuredUpdater()
        return NormalItemUpdater()

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update(item)