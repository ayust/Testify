# Copyright 2009 Yelp
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from testify import *

class TurtleTestCase(TestCase):
    @setup
    def build_turtle(self):
        self.leonardo = turtle.Turtle()

    def test_call(self):
        """Just call a turtle"""
        assert self.leonardo()

    def test_attribute(self):
        """Check our attribute access"""
        assert self.leonardo.is_awesome().and_can_chain().whatever_he_wants()

    def test_call_record(self):
        """Check that calls are recorded"""
        self.leonardo(1, 2, 3, quatro=4)
        assert_equal(len(self.leonardo.calls), 1)
        assert_equal(self.leonardo.calls, [((1,2,3), {"quatro": 4})])
    
    def test_attribute_setting(self):
        """Check that we can set attributes and pull them back out"""
        self.leonardo.color = "blue"
        assert_equal(self.leonardo.color, "blue")
    
    def test_attribute_persistence(self):
        """When an attribute is built, it should be persisted"""
        weapon = self.leonardo.weapon
        assert_equal(weapon, self.leonardo.weapon)
        assert weapon is self.leonardo.weapon
        