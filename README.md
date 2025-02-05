# Stannum
![Gradient Tests](https://github.com/ifsheldon/stannum/actions/workflows/run_tests.yaml/badge.svg)

PyTorch wrapper for Taichi data-oriented class

**PRs are welcomed, please see TODOs.**

## Usage

```python
from stannum import Tin
import torch

data_oriented = TiClass()  # some Taichi data-oriented class 
device = torch.device("cpu")
kernel_args = (1.0,)
tin_layer = Tin(data_oriented, device=device)
    .register_kernel(data_oriented.forward_kernel, *kernel_args, kernel_name="forward")  # on old Taichi
    # .register_kernel(data_oriented.forward_kernel, *kernel_args)  # on new Taichi
    .register_input_field(data_oriented.input_field)
    .register_output_field(data_oriented.output_field)
    .register_internal_field(data_oriented.weight_field, name="field name")
    .finish() # finish() is required to finish construction
output = tin_layer(input_tensor)
```

Note: 

It is **NOT** necessary to have a `@ti.data_oriented` class as long as you correctly register the fields that your kernel needs for forward and backward calculation. Please use `EmptyTin` in this case.

For input and output:

* We can register multiple `input_field`, `output_field`, `weight_field`.
* At least one `input_field` and one `output_field` should be registered.
* The order of input tensors must match the registration order of `input_field`s.
* The output order will align with the registration order of `output_field`s.

## Installation & Dependencies
Install `stannum` with `pip` by 

`python -m pip install stannum`

Make sure you have the following installed:
* PyTorch
* Taichi

## TODOs

### Documentation

* Documentation for users

### Features
* PyTorch-related:
  * PyTorch checkpoint and save model
  * Proxy `torch.nn.parameter.Parameter` for weight fields for optimizers
* Python related:
  * @property for a data-oriented class as an alternative way to register
* Taichi related:
  * Wait for Taichi to have native PyTorch tensor view to optimize performance(i.e., no need to copy data back and forth)
  * Automatic Batching - waiting for upstream Taichi improvement
    * workaround for now: do static manual batching, that is to extend fields with one more dimension for batching

### Misc

* A nice logo
