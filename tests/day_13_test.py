import src.day13.part_1
import src.day13.part_2

def test_part_1():
  assert src.day13.part_1.main() == 807

def test_part_2():

  code = """#     ##  #  # ####  ##  #  # ####   ##
#    #  # #  # #    #  # #  # #       #
#    #    #### ###  #    #  # ###     #
#    # ## #  # #    # ## #  # #       #
#    #  # #  # #    #  # #  # #    #  #
####  ### #  # ####  ###  ##  ####  ## """

  assert src.day13.part_2.main() == code
  

