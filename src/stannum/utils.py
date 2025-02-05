from taichi import __version__ as __ti_version


def check_field_needs_grad(field, needs_grad):
    """
    Checks if the Taichi in use is new enough to support automatic grad configuration based on field.snode.needs_grad
    :param field: a Taichi field
    :param needs_grad: boolean or None
    :return: boolean, whether a field needs gradients
    """
    is_legacy_taichi = __ti_version < (0, 7, 26)
    if needs_grad is None:
        if is_legacy_taichi:
            raise Exception(
                f"You are using legacy Taichi (v{__ti_version[0]}.{__ti_version[1]}.{__ti_version[2]} < v0.7.26), "
                f"you need to specify needs_grad yourself when registering a field")
        else:
            return field.snode.needs_grad
    return needs_grad


def autofill_kernel_name_available(kernel):
    """
    check if the taichi implementation have func.__name__ in a @ti.kernel method of a @ti.data_oriented class
    @param kernel: a @ti.kernel function/method
    @return: if support autofill kernel name
    """
    is_legacy_taichi = __ti_version <= (0, 7, 26)
    return not is_legacy_taichi or hasattr(kernel, "__name__")
