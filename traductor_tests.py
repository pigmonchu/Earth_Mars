import unittest
import traductor

class TestTransformation(unittest.TestCase):
    def testToAngles(self):
        self.assertEqual(traductor.num_to_angles(32), (45.0, 0))

    def testToChar(self):
        self.assertEqual(traductor.pair_angles_to_num((90.0, 337.5)), 79)

    def testCharsAlphabetics(self):
        self.assertEqual(traductor.receive([(90.0, 180.0), (135.0, 337.5), (135.0, 270.0), (135.0, 22.5)]), "Hola")

    def testComplexText(self):
        self.assertEqual(traductor.receive( 
                            [(90.0, 180.0), (135.0, 337.5), (135.0, 270.0), (135.0, 22.5),
                             (45.0, 270.0), (45.0, 0.0), (0.0, 225.0),
                             (90.0, 292.5), (157.5, 112.5), (135.0, 315.0), (135.0, 90.0), (135.0, 337.5), (45.0, 22.5)
                            ]
                        ), "Hola, \nMundo!")


class TestOfToEarth(unittest.TestCase):
    def testOneChar(self):
        self.assertEqual(traductor.send("H"), [(90.0, 180.0)])

    def testCharsAlphabetics(self):
        self.assertEqual(traductor.send("Hola"), [(90.0, 180.0), (135.0, 337.5), (135.0, 270.0), (135.0, 22.5)])

    def testComplexText(self):
        self.assertEqual(traductor.send("Hola, \nMundo!"), 
                            [(90.0, 180.0), (135.0, 337.5), (135.0, 270.0), (135.0, 22.5),
                             (45.0, 270.0), (45.0, 0.0), (0.0, 225.0),
                             (90.0, 292.5), (157.5, 112.5), (135.0, 315.0), (135.0, 90.0), (135.0, 337.5), (45.0, 22.5)
                            ]
                        )

class TestOfToMars(unittest.TestCase):
    def testOneChar(self):
        self.assertEqual(traductor.receive([(90.0, 180.0)]), "H")


if __name__ == '__main__':
    unittest.main()