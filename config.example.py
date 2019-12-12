#Main plasma parameters

#grid_steps = 513; grid_step_size = .03  # 15.39
#grid_steps = 641; grid_step_size = .025  # 16.025
grid_steps = 769; grid_step_size = .02  # 15.38
#grid_steps = 1537; grid_step_size = .01 # 15.37

#xi_step_size = .03
#xi_step_size = .025
xi_step_size = .02
#xi_step_size = .01
xi_steps = int(3000 // xi_step_size)

# Diagnostic parameters #

#diagnostics_each_N_steps = int(1 / xi_step_size)
#diagnostics_each_N_steps = int(.1 / xi_step_size)
diagnostics_each_N_steps = 1

diagnostic_ro_each_N_steps = int(1 / xi_step_size)

pic_ro_limit = 0.01

derivate_each_N_steps = int(10 / xi_step_size)

# Noise reduction parameters #

#noise_red_each_N_steps = int(0.25 / xi_step_size)
noise_red_each_N_steps = 1

n_pass = 4

log_Ez_start = int(2985 / xi_step_size)
log_Ez_end = int(3000 / xi_step_size)

# Additional plasma parameters #

field_solver_subtraction_trick = 1
field_solver_variant_A = True

reflect_padding_steps = 5
plasma_padding_steps = 10
plasma_coarseness, plasma_fineness = 3, 2

from numpy import cos, exp, pi, sqrt

def beam(xi_i, x, y):
    xi = -xi_i * xi_step_size
    COMPRESS, BOOST, SIGMA, SHIFT = 1, 5, 1, 0
    if xi < -2 * sqrt(2 * pi) / COMPRESS:
        return 0
    r = sqrt(x**2 + (y - SHIFT)**2)
    return (.05 * BOOST * exp(-.5 * (r / SIGMA)**2) *
            (1 - cos(xi * COMPRESS * sqrt(pi / 2))))

gpu_index = 0
