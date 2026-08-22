from pyats import aetest
from genie.testbed import load


class InterfaceTest(aetest.Testcase):

    @aetest.setup
    def setup(self, testbed):
        self.device = testbed.devices['RTR02']    # match your real hostname
        self.device.connect(log_stdout=False)

    @aetest.test
    def test_gig1_up(self):
        parsed = self.device.parse('show ip interface brief')
        status = parsed['interface']['GigabitEthernet1']['status']
        if status != 'up':
            self.failed(f"Gig1 is {status}, expected up")

    @aetest.cleanup
    def cleanup(self):
        self.device.disconnect()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=load)
    args, unknown = parser.parse_known_args()

    aetest.main(testbed=args.testbed)
