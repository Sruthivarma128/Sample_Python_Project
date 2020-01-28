
def test_add(operand1, operand2, expectedResult):
  cal = Calculator()
  assert cal.add(operand1, operand2) == expectedResult

def test_subtract(operand1, operand2, expectedResult):
  cal = Calculator()
  assert cal.subtract(operand1, operand2) == expectedResult


#@pytest.fixture()
#def setup():
#  print("\nSetup")
#  yield 5
#  print("\nTear down 1")
#
#@pytest.fixture()
#def setup1(request):
#  print("\nSetup1")
#  def teardown_a():
#    print("\nTear down A")
#  def teardown_b():
#    print("\nTear down B")
#  
#  request.addfinalizer(teardown_a)
#  request.addfinalizer(teardown_b)


