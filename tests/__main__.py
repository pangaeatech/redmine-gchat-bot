import logging, unittest
from tests import xmlrunner
from tests.trigger.init import TestTrigger

def run(xml=None):
    logger = logging.getLogger('')
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S'))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTrigger))

    if xml is not None:
        runner = xmlrunner.XMLTestRunner()
        runner._path = xml
    else:
        runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    return len(results.failures) + len(results.errors)

if __name__ == '__main__':
    outdir = sys.argv[1] if len(sys.argv) == 2 else None
    sys.exit(run(outdir))

