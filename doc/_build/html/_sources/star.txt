恒星的物理参数
===============

有效温度
---------

1. 用 Fe I 线的激发平衡，也就是不同低能级激发电势的 FeI 线给出的丰度一致。例如 Santos et al. 2004 [#Santos2004]_, Santos et al. 2005 [#Santos2005]_。这种方法的缺点是依赖于大气模型；受到 NLTE 效应的影响，特别是在贫金属星中；对米粒效应敏感。优点是不依赖于红化。

2. 拟合巴耳末线。例如 Fuhrmann et al. 1993 [#Fuhrmann1993]_，Fuhrmann et al. 1994 [#Fuhrmann1994]_，Barklem et al. 2002 [#Barklem2002]_。缺点是依赖大气模型；都对米粒效应敏感。优点是都不依赖于红化。

3. 用颜色—有效温度的经验关系。通常采用以下公式进行拟合：

   .. math::
       \theta_\mathrm{eff} = a_0 + a_1X + a_2X^2 + a_3X[\mathrm{Fe/H}] + a_4[\mathrm{Fe/H}] + a_5[\mathrm{Fe/H}]^2


表面重力
---------

恒星的表面重力与质量、半径的关系为：

.. math::
   \log_{10}{g_*} = \log_{10}{\left(\frac{M_*}{M_\odot}\right)} - 2\log_{10}{\left(\frac{R_*}{R_\odot}\right)} + \log_{10}{g_\odot}

恒星的表面重力与质量、有效温度的关系为：

.. math::
    \log_{10}{g}=\log_{10}{g_\odot}+\log_{10}\left(\frac{M}{M_\odot}\right)+4\log_{10}\left(\frac{T_{\mathrm{eff}}}{T_{\mathrm{eff},\odot}}\right)+0.4(M_{\mathrm{bol}}-M_{\mathrm{bol},\odot})

其中 *M*:sub:`bol` 是绝对热星等。

如果表面重力是由三角视差测定的，三角视差（距离）测量的不确定性会直接影响表面重力的误差。由于

.. math::
    M_{\mathrm{bol}}=V_{\mathrm{mag}}+BC-5\log_{10}{d}+5-A_{\mathrm{V}}

把距离与三角视差的关系 \\ref{d_para} 式代入得到：

.. math::
    M_{\mathrm{bol}}=V_{\mathrm{mag}}+BC+5\log_{10}{\varpi}-10-A_{\mathrm{V}}

因此

.. math::
    \frac{\partial\log_{10}{g}}{\partial\varpi}=\frac{2}{\varpi\ln10}\simeq0.87\frac{1}{\varpi}

由上式可知，10% 的三角视差误差会导致表面重力大约 0.087 dex 的误差；15% 的测量误差会导致 0.13 dex 的误差；20% 的测量误差会导致 0.17 dex 的误差。



.. csv-table:: Mass of central black hole
    :header: "*M*:sub:`BH` (10\ :sup:`6` Msun)", "References"
    :widths: 20, 40

    "3.61 ± 0.32",                     "Eisenhauer et al. 2005 "
    "4.1 ± 0.4",                       "Morris et al. 2012 "
    "5.76 :sup:`+1.76`\ :sub:`−1.26`", "Do et al. 2013 "
    "4.0",                             "Fragione et al. 2017 "


.. currentmodule:: naoctest.subpack1.fitting
.. autosummary::
    test
    

.. automodule:: naoctest.subpack1.fitting
    :members:
    :private-members:

参考文献
---------

.. [#Allen1976] Allen, C., 1976, *Astrophysical Quantities*, London: Athlone (3rd edition) :ads:`1976asqu.book.....A`
.. [#Alonso1996] Alonso et al., 1996, A&A, 313, 873 :ads:`1996A%26A...313..873A`
.. [#Alonso1999] Alonso et al., 1999, A&AS, 140, 261 :ads:`1999A%26AS..140..261A`
.. [#Alonso2001] Alonso et al., 2001, A&A, 376, 1039 :ads:`2001A%26A...376.1039A`
.. [#Andersen1999] Andersen, 1999, *IAUTB*, 23, p. 182 and 141 :ads:`1999IAUTB..23.....A`
.. [#Barklem2002] Barklem et al., 2002, A&A, 385, 951 :ads:`2002A%26A...385..951B`
.. [#Bessell1998] Bessell et al., 1998, *A&A*, 333, 231 :ads:`1998A%26A...333..231B`
.. [#Blackwell1977] Blackwell & Shallis, 1977, MNRAS, 180, 177 :ads:`1977MNRAS.180..177B`
.. [#Blackwell1979] Blackwell et al., 1979, MNRAS, 188, 847 :ads:`1979MNRAS.188..847B`
.. [#Casagrande2010] Casagrande et al., 2010, A&A, 512, A54 :ads:`2010A%26A...512A..54C`
.. [#Cox2000] Cox, 2000, *Allen's astrophysical quantities*, 4th ed. Publisher: New York: AIP Press; Springer :ads:`2000asqu.book.....C`
.. [#Durrant1981] Durrant, C.J., 1981, *Landolt Bornstein* vol VI/2A, (Neue Series: Springer-Verlag), p82
.. [#Edvardsson1993] Edvardsson et al., 1993, *A&A*, 275, 101 :ads:`1993A%26A...275..101E`
.. [#Flower1996] Flower, 1996, *ApJ*, 469, 355 :ads:`1996ApJ...469..355F`
.. [#Fuhrmann1993] Fuhrmann et al., 1993, A&A, 271, 451 :ads:`1993A%26A...271..451F`
.. [#Fuhrmann1994] Fuhrmann et al., 1994, A&A, 285, 585 :ads:`1994A%26A...285..585F`
.. [#GonzalezHernandez2009] González Hernández & Bonifacio, 2009, A&A, 497, 497 :ads:`2009A%26A...497..497G`
.. [#Gratton2003] Gratton et al., 2003, *A&A*, 404, 187 :ads:`2003A%26A...404..187G`
.. [#Houdashelt2000] Houdashelt et al., 2000, AJ, 119, 1448 :ads:`2000AJ....119.1448H`
.. [#IAU2015] `IAU XXIX General Assembly Draft Resolutions Announcement <http://www.iau.org/news/announcements/detail/ann15023/>`_
.. [#Lang1991] Lang, K.R., 1991, *Astrophysical Data: Planets and Stars* (Springer-Verlag), p103
.. [#Masana2006] Masana et al., 2006, A&A, 450, 735 :ads:`2006A%26A...450..735M`
.. [#Onehag2009] Önehag et al., 2009, A&A, 498, 527 :ads:`2009A%26A...498..527O`
.. [#Ramirez2005] Ramírez & Meléndez, 2005, ApJ, 626, 465 :ads:`2005ApJ...626..465R`
.. [#Reddy2003] Reddy et al., 2003, *MNRAS*, 340, 304 :ads:`2003MNRAS.340..304R`
.. [#Santos2004] Santos et al., 2004, A&A, 415, 1153 :ads:`2004A%26A...415.1153S`
.. [#Santos2005] Santos et al., 2005, A&A, 437, 1127 :ads:`2005A%26A...437.1127S`
.. [#Schmidt-Kaler1982] Schmidt-Kaler, Th., 1982, in: *Landolt-Bornstein, Numerical Data and Functional Relationships in Science and Technology*, Vol. 2. (eds.) K. Schaifers & H.H. Voigt Springer-Verlag, Berlin, p.451
