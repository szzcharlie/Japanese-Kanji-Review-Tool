import numpy as np

def generic_test(func: object, input_tuple: tuple, desired_outputs: tuple):
    """Test whether the real output of a function given a specific input
    matches the desired output.

    Args:
      func: the function object that is used for the test.
      input_tuple: a tuple that includes all of the required inputs
        of the function.
      desired_outputs: a tuple that includes all of the desired
        outputs of the function.
    Returns:
      None
    """
    print("Function '",func.__name__,"' is being tested.", sep = "")
    try:
        print("The input arguments are", *input_tuple)
        print("The outputs expected are", *desired_outputs)
    except TypeError:
        print("You are not using tuples for your inputs or desired outputs.")
        raise
    except:
        raise
    try:
        actual_output = func(*input_tuple)
        print("The actual outputs are", actual_output)
        if len(desired_outputs) == 1:
            desired_outputs = desired_outputs[0]
        if type(desired_outputs) == np.ndarray:
            assert (func(*input_tuple) == desired_outputs).all(), f"Output of the function does not match the desired output."
        elif type(desired_outputs) == list:
            assert type(actual_output) == list, f"Output of the function does not match the desired output."
            assert len(actual_output) == len(desired_outputs), f"Output of the function does not match the desired output."
            for i in range(0, len(desired_outputs)):
                if type(desired_outputs[i]) == np.ndarray:
                    assert (actual_output[i] == desired_outputs[i]).all(), f"Output of the function does not match the desired output."
                else:
                    assert actual_output[i] == desired_outputs[i], f"Output of the function does not match the desired output."
        else:
            assert actual_output == desired_outputs, f"Output of the function does not match the desired output."
    except TypeError:
        print("Your input tuple does not have the right type for the function.")
        raise
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        raise
    except AssertionError:
        print("Output of the function does not match the desired output.")
        print("The test failed.\n")
        raise
    except:
        raise
    else:
        print("The test passed.\n")
