from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("guichet-unique")])
class TestGuichetUnique(ArtemisTestFixture):
    """
    """
    def test_guichet_unique_caen_to_marseille(self):
        """
        ID artemis v1: 0
        """
        self.journey(_from="admin:149197extern",
                     to="admin:76469extern", datetime="20120924T070000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_rouen(self):
        """
        ID artemis v1: 1
        """
        self.journey(_from="admin:7444extern",
                     to="admin:75628extern", datetime="20121012T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_caen_to_brest(self):
        """
        ID artemis v1: 2
        """
        self.journey(_from="admin:149197extern",
                     to="admin:1076124extern", datetime="20121022T054500",
                     walking_speed="0.83", max_duration_to_pt="240", count="7", type="rapid")

    def test_guichet_unique_reims_to_paris(self):
        """
        ID artemis v1: 18
        """
        self.journey(_from="admin:36458extern",
                     to="admin:7444extern", datetime="20121020T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1481", raises=AssertionError)
    def test_guichet_unique_avignon_to_marseille(self):
        """
        ID artemis v1: 19
        """
        self.journey(_from="admin:102478extern",
                     to="admin:76469extern", datetime="20120928T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_avignon(self):
        """
        ID artemis v1: 20
        """
        self.journey(_from="admin:7444extern",
                     to="admin:102478extern", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_ay(self):
        """
        ID artemis v1: 21
        """
        self.journey(_from="admin:7444extern",
                     to="admin:417494extern", datetime="20121121T120000",
                     walking_speed="0.83", max_duration_to_pt="240")

    def test_guichet_unique_paris_to_Avenay_Val_d_Or(self):
        """
        ID artemis v1: 22
        """
        self.journey(_from="admin:7444extern",
                     to="admin:2651291extern", datetime="20121025T120000",
                     walking_speed="0.83", max_duration_to_pt="6000")
