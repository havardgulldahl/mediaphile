import os
import unittest
from mediaphile.lib.file_operations import generate_filename_from_date, generate_folders_from_date

from mediaphile.lib.photos import get_photos_in_folder, get_date_from_file
from mediaphile.lib.metadata import get_metadata, get_exif


class CanonTests(unittest.TestCase):
    """
    Tests the most basic functions and methods in photofile, in relation to photos produced using Canon cameras.
    """

    def setUp(self):
        """
        Creates some default data to base our tests on.
        """
        self.source_folder = os.path.join(os.curdir, 'Canon')

    def test_get_photos(self):
        """

        """
        for folder, filenames in get_photos_in_folder(self.source_folder).items():
            for filename in filenames:
                complete_filename = os.path.join(folder, filename)
                print(get_metadata(complete_filename))
                print(get_exif(complete_filename))
                dt = get_date_from_file(complete_filename)
                print(dt)
                print(generate_filename_from_date(complete_filename, dt))
                print(generate_folders_from_date(dt))

        #self.assertEqual(self.seq, range(10))
        #self.assertRaises(TypeError, random.shuffle, (1,2,3))
        ## self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest.main()