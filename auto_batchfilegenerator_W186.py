import numpy as np


main_str = """# where to load the gainshifts from; one can also use:
#   parameter gain_e = ...
# and so on
#gain file gainshifts_013.dat
gain file gainshifts_plain.dat


# (constant fraction) cactus energy correction parameters for cactus time
parameter tnai_corr_enai = 0 1 0 0 // use these!
#parameter tnai_corr_enai = -5.52368 18201.9 210.387 -0.00125989 // comment out

# (constant fraction) siri energy correction parameters for cactus time
parameter tnai_corr_esi  = 0 1 0 0  // use these!
#parameter tnai_corr_esi  = 50.4471 -475514 4506.25 -0.00185164 // comment out

################ Only when PPACs are used ##################################
# (constant fraction) engery/time correction parameters for PPAC
# The correction for the PPAC coutners are necessary due to SiRi, so
# usually the same corrections parmeters as in tnai_corr_esi should be used
# ### comment out this line(s) if no PPACs are used
# parameter tppac_corr_esi = 0 1 0 0
#parameter tppac_corr_esi  =  50.4471 -475514 4506.25 -0.00185164
############################################################################

# Parameters for the range curve, 3He or alpha
#rangefile zrange_he3.dat
#rangefile zrange_a.dat
rangefile zrange_d.dat
#rangefile zrange_p.dat

# Cut of low-energy events by making a rectangle which is excluded
# in the down, left corner of the banana. 
# Contains E-minimum 1, DE-minimum 1, E-minimum 2, DE-minimum 2.
# Including Z=1 particles:
parameter ede_rect  = 500 250 30 500
# Excluding Z=1 particles:
#parameter ede_rect  = 500 2500 2000 2500

# Thickness gate for proton banana
# parameter thick_range = 82 12 0
parameter thick_range = 125 15 0
# parameter thick_range = 140 20 0
# parameter thick_range = 276 75 0
# parameter thick_range = 230 25 0

# Thickness gate for 3He banana FIND D
#parameter thick_range = 48 8 0

# Thickness gate for alpha banana
#parameter thick_range = 165 10 0
#parameter thick_range = 48 5 0

# Fit of rkinz column 1 as function of rkinz column 6. No. Using Qkinz.
#  186W (alpha, d gamma) 188Re, 30MeV. Strip 0-7 in that order. Deutron-data! [keV]
parameter ex_from_ede    = 1.4551283+4 -1.000915 -8.04e-7 \
1.4556803e+4 -1.000073 -8.18e-7 \
1.4561938+4 -9.999144e-1 -8.33e-7 \
1.4567338e+4 -9.98259e-1 -8.45e-7 \
1.4572350e+4 -9.97292e-1 -8.60e-7 \
1.4576298e+4 -9.96112e-1 -8.82e-7 \
1.4580493e+4 -9.94982e-1 -9.00e-7 \
1.4584253e+4 -9.93772e-1 -9.21e-7

# empirical excitation energy correction for the above, e.g. from known peaks
parameter ex_corr_exp    =  0 1 \
    0 1 \
    0 1 \
    0 1 \
    0 1 \
    0 1 \
    0 1 \
    0 1

# NaI time gates, for making the ALFNA matrices 
# found by looking at the m_nai_t plot and projecting it
# down to the x-axis/m_nai_e_t_c x-axis plot 
# remember to subtract the same amount of channels 
# as the ones that are filled, and make sure you "hit" a top!
# parameter = lower cut of prompt ,     higher gate of prompt peak,  \
#             lower cut on backgr.,     higher cut backgr.
parameter nai_time_cuts = 190 220 \
                          300 330

############## Attention when no PPACs are used ###########################
# define id of NaI detectors and PPAC detectors (need to change usersort for more then four PPACs!)
# All other channel are considered as NaI detectors. In case you don't use fission detectors,
# define this parameters as "-1" - all id's are positive numbers, thus none will match -1.
# ### Corresponding line /without/ fission detectors:
# parameter channel_PPAC = -1 -1 -1 -1
# ### Corresponding line /with/ fission detectors: [adopt channel numbers]
parameter channel_PPAC = 4 12 30 31                          

################ Only when PPACs are used ##################################
# PPAC time gates
# time gates of the ppacs are found from the fission blob 
# in the m_siri_e_t_ppac plot (fission blob in tPPAC vs E_SiRi gate)
# - time gates from the y-axis, and energy from the x-axis
# parameter = lower cut of prompt ,     higher gate of prompt peak,  \
#             lower cut on backgr.,     higher cut backgr.
# ### comment out this line(s) if no PPACs are used
#parameter ppac_time_cuts = 190 200 \
#                           290 300

# Energy gate on fission
# the energy gate is found by looking at the 
# m_siri_e_t_ppac plot (fission blob in tPPAC vs E_SiRi gate) 
# - it should be roughly the fission barrier
# (Fission starts at some point, only events with 
# a higher energy than excitation_energy_min can be true fission events)
# ### comment out this line(s) if no PPACs are used
parameter fission_excitation_energy_min = 5000  # in keV

# Total efficiency of the PPACs in 4Pi
parameter ppac_efficiency = 0.48
############################################################################

#data directory Datafiles
data directory ../master_data/raw

#maximum number of buffers to read for each file; for testing
#max_buffers 1 
"""

files = ["""sirius-20160420-135618.data""",
"""sirius-20160420-171400.data""", 
"""sirius-20160420-182451.data""",
"""sirius-20160420-233716.data""",
"""sirius-20160421-091709.data""",
"""sirius-20160421-100724.data""",
"""sirius-20160421-224045.data""",
"""sirius-20160422-081940.data""", 
"""sirius-20160422-093300.data
sirius-20160422-093300-big-0,00.data
sirius-20160422-093300-big-0,01.data""",
"""sirius-20160422-122054.data""",
"""sirius-20160422-124416.data""",
"""sirius-20160422-180843.data""",
"""sirius-20160423-073059.data""",
"""sirius-20160423-160731.data""",
"""sirius-20160423-173835.data""",
"""sirius-20160423-213756.data""",
"""sirius-20160424-104217.data""",
"""sirius-20160424-160703.data""",
"""sirius-20160424-223103.data""",
"""sirius-20160425-075414.data""",
"""sirius-20160425-120131.data""",
"""sirius-20160425-203224.data""",
"""sirius-20160425-222023.data""",
"""sirius-20160426-104456.data""",
"""sirius-20160426-120853.data""",
"""sirius-20160426-141446.data""",
"""sirius-20160426-230123.data""",
"""sirius-20160427-033555.data""",
"""sirius-20160428-091134.data""",
"""sirius-20160428-122211.data""",
"""sirius-20160428-173419.data""",
"""sirius-20160428-230248.data""",
"""sirius-20160429-070605.data""",
"""sirius-20160429-094446.data
sirius-20160429-094446-big-000.data
sirius-20160429-094446-big-001.data
sirius-20160429-094446-big-002.data
sirius-20160429-094446-big-003.data"""]



# Write to MAMA matrix 
#export mama h_ex_f0 h_ex_f0_MAMA
#export mama m_alfna alfna
#export mama m_alfna_bg alfna_bg

# at the end, spectra are dumped to the root file
# root output file
export root W186_raw_"""sirius-20160422-093300.data""",.root






