# Abstract

This is the source codes for the nested equivalence source approximation (NESA) for multiscale electromagnetic (EM) simulations. It is employed to approximate the Green’s function matrix G(r, r')=exp(-jk|r-r'|)/|r-r'|​ with NESA with a predetermined threshold. The approximation error is determined by the number of equivalence points. The computation complexities for low and high frequency EM problems are O(N) and O(NlogN)​, respectively. Please see the reference for more details. It is easy to apply it to accelerate the existing method of moments (MoM) codes. 

# Reference

[1] M. Li, M. A. Francavilla, F. Vipiana, G. Vecchi, and R. S. Chen, “Nested equivalent source approximation for the modeling of multiscale structures,” IEEE Trans. Antennas Propag., vol. 62, no. 7, pp.  664-3678, Jul. 2014.

[2] M. Li, M. A. Francavilla, R. S. Chen, and G. Vecchi, “Wideband fast kernel independent modeling of large multiscale structures via nested equivalent source approximation,” IEEE Trans. Antennas Propag., vol. 63, no. 5, pp. 2122–2134, May 2015.

[3] M. Li, M. A. Francavilla, R. Chen, and G. Vecchi, “Nested equivalent source approximation for the modeling of penetrable bodies,” IEEE Trans. Antennas Propag., vol. 65, no. 2, pp. 954–959, Feb. 2017.

[4] M. Li, M. A. Francavilla, D. Ding, R. Chen, and G. Vecchi, “Mixed-form nested approximation for wideband multiscale simulations,” IEEE Trans. Antennas Propag., vol. 66, no. 11, pp. 6128–6136, Nov. 2018.