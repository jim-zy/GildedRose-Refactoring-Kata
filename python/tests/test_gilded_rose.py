# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_increases_in_quality_twice_after_expiration(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_conjured_items_degrade_twice_as_fast_as_normal_items(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    # Comprehensive BackstagePass tests
    def test_backstage_passes_increase_by_1_when_more_than_10_days(self):
        """Backstage pass increases by 1 when sell_in > 10"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increase_by_2_when_6_to_10_days(self):
        """Backstage pass increases by 2 when sell_in is between 6 and 10 (inclusive)"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_by_2_when_6_days_before_concert(self):
        """Backstage pass at boundary: 6 days increases by 2"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_by_3_when_1_to_5_days(self):
        """Backstage pass increases by 3 when sell_in is between 1 and 5 (inclusive)"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_increase_by_3_when_1_day_before_concert(self):
        """Backstage pass on final day increases by 3"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_quality_capped_at_50(self):
        """Backstage pass quality never exceeds 50"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)  # 49 + 3 = 52, but capped at 50

    def test_backstage_passes_quality_capped_at_50_after_expiration(self):
        """Backstage pass quality becomes 0 after concert (not affected by quality cap)"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
