# -*- coding: utf-8 -*-

from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, \
    utils, send_ire, get_last_rt_loaded_time, wait_for_rt_reload

@dataset([DataSet("sncf")])
class TestRealTime(ArtemisTestFixture):
    """
    test RealTime on SNCF
    """

    def test_normal_train(self):
        """
        Requested departure: 2015/12/15 14:20
        From: Gare de Lyon, Paris
        To: Saint Charles, Marseilles

        we should find a train travelling from 14:37 to 17:54
        """
        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="base_schedule")

    def test_cancel_train(self):
        """
        test cancellation of the train

        Requested departure: 2015/12/15 14:20
        From: Gare de Lyon, Paris
        To: Saint Charles, Marseilles

        Before the cancellation, we should find a train travelling from 14:37 to 17:54
        After the cancellation, a train travelling from 15:37 to 18:54 will be found
        """
        last_rt_data_loaded = get_last_rt_loaded_time(COVERAGE)

        # TGV
        send_ire('trip_removal_tgv_2913.xml')
        # iDTGV
        send_ire('trip_removal_tgv_6154.xml')

        wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151215T1420",
                     data_freshness="realtime")

    def test_repeat_the_same_ire_and_reload_from_scratch(self):
        """
        test cancellation of the train

        Requested departure: 2015/12/20 17:00
        From: Gare de Lyon, Paris
        To: Saint Charles, Marseilles

        After the cancellation, a train travelling from 18:37 to 21:54 should be found
        """
        last_rt_data_loaded = get_last_rt_loaded_time(COVERAGE)

        for i in range(5):
            send_ire('trip_removal_tgv_6123.xml')

        wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151220T1700",
                     data_freshness="realtime")

        """
        At this point, an IRE is saved into the db,
        now we'll test the case where kraken is run from scratch and the previous
        IRE should be taken into account
        """
        last_rt_data_loaded = get_last_rt_loaded_time(COVERAGE)

        self.kill_the_krakens()
        self.pop_krakens()

        wait_for_rt_reload(last_rt_data_loaded, COVERAGE)

        self.journey(_from="stop_area:OCE:SA:87686006",
                     to="stop_area:OCE:SA:87751008",
                     datetime="20151220T1700",
                     data_freshness="realtime")

