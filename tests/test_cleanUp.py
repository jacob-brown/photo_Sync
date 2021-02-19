import cleanUp
import os


def test_removeFile():
    filename = "test_tmp_check_deleted"
    open(filename, "w")
    cleanUp.removeFile(filename)
    result_bool = not os.path.exists(filename)
    assert result_bool


def test_removeBlankLines():
    filename = "test_tmp_check_no_lines"

    with open(filename, "w") as writer:
        for i in range(0, 10):
            writer.writelines("\n")

    cleanUp.removeBlankLines(filename)
    with open(filename, "r") as reader:
        line = reader.readlines()
        assert not line == "\n"

    cleanUp.removeFile(filename)