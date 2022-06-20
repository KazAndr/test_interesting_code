      implicit real*8 (a-h,o-z)
      Real*8 lek1,lpoC(20),lpCP(4),lg,l25,lpPits,lpoC0,le1,lekb,
     *	     lpop,lekbp,lo,lef,lp25,lcp
      character*9 Mp1(9),NAME
      CoMMoN /HACTP/ NAchzoH,NApl,Nz0,KBMAX
      CoMMoN /prog/ PEz(201,17),Al(1024)
      CoMMoN /KBobM/ MTKB(40,3),IKB,Mp1
      CoMMoN /pAP1/ R,R2,RM,KgAPM,Tf,JLLL(2),KSoPb,flpAd(2)
     *		  ,HPHo(2),KoPbo,kbet1,ksw1
      CoMMoN /pAPT/ V,HMM,Rz,RMM,chM,pX,DCg(3),TETR,TzTPC,KlDTB
     *		,Kf514
      CoMMoN /pAP/ SoPb,H,F,F81,AP
      CoMMoN /PEziM/ KdB,KBub1,KBub2,KoP1,KCTAb1,KoP2,
     * KCTAb2,K2BKl,KTPAC,KtsiKl,KbC,KCPuB,KyC,KPyC,KoP,
     * KCTAb,KBub,KAC,KpEchf,KpC,Kbob,Kboy,KPEziM,KlaM
     *	      ,KBAPpl,KBET,KSW,NMEC,KopoP,KoA
      CoMMoN /PEz615/ KK,KP,KPS,NKPA,KBAPe,KPACC,DpPp,DpPM
     *	      ,HP615,Koldpo,DTdpo,hdecay
      CoMMoN /oBJECT/ GA0,GCA,Tag1,ydTag1,Tag2,ydTag2,Tag,ydTag,
     *		      XT,yT,SCA,ALb(6),STEK,GTEK,Tdy1,Tdy2
      CoMMoN /yCTAB/ TBKl1,DV1,p1,g1,TET1,TBKl2,DV2,p2,g2,TET2,
     *		     DTAy,DTPAzd,SKPEH,DELTT,DK,DT0,TC,ANPyC,
     *		     AKPyC0,ToP,PAzB(3),TBKl,DV,gKoM,TPAzd,HPAzd
     *		    ,lpoC0
     
      common /USTTMA/ dtvn,anaus,akaus,vsr,ayt,fipos0,klpar
      
     
      common /DISPTMA/ dAld,dCxd,dCyd,dVsd,nvar,ixx,iyy,rdal1,rdal2,
     *                 rdk1,rdk2,rdcx1,rdcx2,rmx0,rdtraz,rdtpr,krass
           
     
      common /RMDTMA/ tvsi1(37),altrack
      
      common /RANVAR/ rgam(12),ret(12),rtro(15)
      
      common /PARACHUT/ parampar(3)
      
      common /REZDPO/ kdpopod,ag0,ap0,ar0,adp,aa1

      CoMMoN /PEzMd/ eTAp(11,10),TPAC(160,10),TPCPuB(20,10),
     *	  NTTPAC(2),fg,lg,TVSI(288),TVHp(8,3),TH104,T1Cyd,V1Cyd
     *	  ,T2Cyd,V2Cyd,lpPits,AVKP(2),fippish
     
      Common /form522/ DVtorm, k_altitude_off, DV_522(13), k522, 
     <              kmax, knumber, Enangle512 

      DIMENSIoN BiT(20),TBKf(20),CyTB(20),ygldA(20),fpoC(20),
     *          XPHy(20),XPid(25),TpCP(4),fpCP(4),ApCP(4),wet(3)
      DIMENSIoN Hy(6),C(17),Ya(6),sozut(20),sozve(20),tenvh(20),
     *          tenvy(20)
      Real*8 Zagl(6)
      DIMENSIoN MKBiT(10),TKPEH(4)
      DIMENSIoN foPMA(5),NHAchB(5),NpoPts(5),NTlg0(5)
      character*60 MshHy(2)
      character*48 Mshid(3)
      character*48 Mid615
      character*3 MTf
      DATA KHy/0/, Kid/0/,JKBiT/1/,KlgpP/0/,Kf14,Kf512/0,0/
      DATA MKBiT/0,0,0,0,0,0,0,0,0,0/
      DATA KBHy/0/,KBid/0/,KBPP,KBPB/0,0/
      DATA pPg/57.2957795056d0/
      Data OMZ/7.29211587d-5/
      DATA Mp1 /'ÒÐÀÕÓÍÎÂ','ÒÐÓÔÀÍÎÂ','ÊÓÄÐßÂÖÅÂ','ÊÓÒÅÏÎÂ',
     *'ÁÀÁÀßÍ',' ','ÑÀÂ×ÅÍÊÎ','ÑÈÍÄÞÊÎÂÀ',''/
      DATA MshHy/
     * '  ÎÁ	 HÓ    BÈTOK    ÄATA	       BPEMß   ',
     * '     X	     Ó	       Z	VX	   VÓ	      VZ'/
      DATA Mshid/
     * '   G	  GÁÎ	  GCA	  P	P ÓÄ	DVT',
     * '    XT       ÓT         SCA',
     * '                                      ÄATA ÈÄ'/
      DATA Mid615 /
     * '    G	   G KAÏC     P    P ÓÄ   DVT	ÄATA ÈÄ'/
      DATA KyX/8137/
      DATA KBCyT /16/
      DATA nz0/14/
      DATA nachzoh /0/
c#################################################
c=================================================

      F=200.d0
      F81=200.d0
      AP=12.d0
      
      kdpopod=0
       
      kbmax=200
      open(72,file='list.rez')

      nz512c=nachzoh+3
 1000 WRITE (*,1)
      KBBHy=0
    1 FoRMAT(15/50X,' >>> BEPCÈß ÎT 10.01.2006 <<<'//
     * 10X,'	            C A Ä È K  -  Ò Ì À	       '/
     *10X,' ( CÏÓCKÎBÎÉ ABTÎMATÈÇÈPÎBAHHÛÉ ÄÈAËÎÃÎBÛÉ KÎMÏËEKC )'//
     * '    ×TÎ HÓÆHÎ? - ÏPÎÃHÎÇ          (1)'/
     * '                 CÏÓCK ÑÎÞÇ ÒÌÀ   (2)'/
     * '                 CÏÓCK ÏÐÎÃÐÅÑÑ Ì (3)'/
     * '                 ÎTHÎÑ. ÄBÈÆEHÈE  (4)'/
     * '                 ÑÎÃËÀÑ. ÌÎÄÅËÅÉ  (5)'/
     * '                 BÛXÎÄ            (0)'//
     * '    BÛÁÈPAÉTE :')
      CALL vvodi('   -->',KPAb)
      NKoH=1
      IF(KPAb.EQ.-9999) Go To 1022
      IF(KPAb.EQ.8137) Go To 1000
      IF(KPAb.LT.0.oR.KPAb.GT.5) Go To 1000
      KP1=KPAb+1
      Go To (10,100,200,7000,3500,3600),KP1
      Go To 1000
 1022 WRITE (*,1023)
 1023 FoRMAT(/'    ×ÈCTÈTÜ APXÈB (1), HET (0) ?')
      IF(JJJ.EQ.KyX) Go To 1000
      CALL vvodi('   -->',JJJ)
      IF(JJJ.EQ.0) Go To 1000
      Do 1024 II=1,1024
 1024 Al(II)=0.
      CALL WRTAPE(Al,1024,4,5,NAchzoH)
      Go To 1000
   10 WRITE (*,3)
    3 FoRMAT(/'    BÛ, KAÆETCß, XÎTÈTE ÇAKÎH×ÈTÜ PAÁÎTÓ C',
     * '  KÎMÏËEKCÎM ?'/
     * '    BBEÄÈTE (0), ECËÈ ÓBEPEHÛ ÈËÈ ×TÎ-HÈÁÓÄÜ ÖEËÎE, ECËÈ',
     * '  HET')
      CALL vvodi('   -->',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.NE.0) Go To 4
      close(72)
      WRITE (*,5)
    5 FoRMAT(/'      HE ÇÀÁÓÄÜÒÅ ÏÎÑÌÎÒÐÅÒÜ ËÈCTÈHÃ (list.rez)!'/
     *	'	     ... ÁËAÃÎÄAPÞ ÇA BHÈMAHÈE .'/)
      SToP
    4 Go To 1000
C	CÏÓCK 732
  200 WRITE (*,400)
  400 FoRMAT(/5X,'    * CÏÓCK ÑÎÞÇ ÒÌÀ *'//
     * '    BÛÁÈPAÉTE: ÔÈÇÈKA+ÔÎPMÛ        (1)'/
     *        11X,'    ÔÎPMÛ               (2)'/
     *        11X,'    APXÈB ÔÈÇÈKÈ È ÔÎÐÌ (3)'/
     *        11X,'    ÇAÏÈCÜ ÔÎÐÌ Â ÁÄ    (4)'/
     *        11X,'    B Û X Î Ä	          (0)')
      ASSIGN 6066 To METob
      CALL vvodi('   -->',Kfiz)
      IF(Kfiz.EQ.KyX) Go To 1000
      IF(Kfiz.EQ.-9999) Go To 920
      IF(Kfiz.LT.0.oR.Kfiz.GT.4) Go To 200
      Kfiz1=Kfiz+1
      Go To (1000,201,950,800,900),Kfiz1
  201 IF(Kfiz.NE.1) Go To 600
  202 WRITE (*,1600)
 1600 FoRMAT(/'    ÇAÄAHÈE ÁPATÜ: C ÝKPAHA  (1)'/15X,
     * '    ÈÇ APXÈBA (2)	(C KTË (-2))'/15X,'    TEKÓÙÈM   (3)')
      CALL vvodi('   -->',K)
      IF(K.EQ.KyX) Go To 10
      IF(K.EQ.3) Go To 204
      IF(K.NE.1.AND.ABS(K).NE.2) Go To 201
      IF(ABS(K).NE.2) Go To 203
      CALL RETAPE(Al,1024,4,5,NAchzoH)
      IF(K.EQ.2) Go To 270
      WRITE (*,272)
  272 FoRMAT(/'               KATAËÎÃ APXÈBA ÇAÄAHÈÉ'//
     * '                Ê-âî              1-é            1-ÿ'/
     * '    Îáë   Âàð   ñòðîê   Ôîðìà    âèòîê  Ïîðöèÿ   òëã ')
      Do 273 I=1,6
      L=360+30*(I-1)-1
      L1=L+1
      L7=L+2
  273 WRITE (*,274)
     * I,nint(Al(L+1)),nint(Al(L+8)),Al(L+9),
     * nint(Al(L+10)),nint(Al(L+11)),nint(Al(L+12))
  274 FoRMAT(I3'.',I5,I7,F10.1,I8,I7,I8)
      write(*,*)
  270 CALL vvodi('   HÎMEP ÎÁËACTÈ (1-6) --> ',Nobl)
      IF(Nobl.EQ.KyX) Go To 1000
      IH=360+30*(Nobl-1)-1
      IF(Nobl.GT.6.oR.Nobl.LT.1) Go To 270
      NzPC=nint(Al(IH+1))
c      Ndz=nint(Al(IH+2))
c      NMz=nint(Al(IH+3))
c      Ngz=nint(Al(IH+4))
c      NHy=nint(Al(IH+5))
c      Nsh=nint(Al(IH+6))
c      Nbb=nint(Al(IH+7))
      KolCTz=nint(Al(IH+8))
      
      Do I=1,KolCTz
        L=IH+4*(I-1)+8
        foPMA(I)=Al(L+1)
        NHAchB(I)=nint(Al(L+2))
        NpoPts(I)=nint(Al(L+3))
        NTlg0(I)=nint(Al(L+4))
      enddo
      
      Nname=nint(Al(IH+29))
      if (Nname.lt.1.or.Nname.gt.9) Nname=3
      NAME=Mp1(Nname)
      Go To 204
  203 KolCTz=1
      JNAME=0
      CALL vvodi('    HÎMEP BAPÈAHTA? --> ',NzPC)
      IF(NzPC.EQ.KyX) Go To 1000
  207 WRITE (*,1601)
 1601 FoRMAT('    BBEÄÈTE HÎMEP ÔÎPMÛ (14,510,511,524,514,521)')
      CALL vvodr('    --> ',foPMA(KolCTz))
      IF(ABS(foPMA(KolCTz)-KyX).LE.0.001d0) Go To 1000
      IF(ABS(foPMA(KolCTz)-514.).LT.0.1
     *.oR.ABS(foPMA(KolCTz)-524.).LT.0.1) CALL fK514(foPMA(KolCTz))
      CALL vvzrs(NHAchB(KolCTz),NpoPts(KolCTz))
      NTlg0(KolCTz)=0
      IF(ABS(foPMA(KolCTz)-514.d0).GT.0.5.
     *	AND.ABS(foPMA(KolCTz)-524.).GT.0.5) Go To 2050
      IF(JNAME.NE.0) Go To 2050  ! Name is already specified !
      WRITE (*,'(/a)') '    KTÎ ÁÓÄET ÏÎÄÏÈCÛBATÜ? (ÂÂÅÄÈÒÅ ÍÎÌÅÐ)'
      do i=1,9 
       	Write(*,'(3x,i4''. ''a11)') i,Mp1(i)
      enddo
 2058 Call VVodi('',Nname)
      if (Nname.LT.1.OR.Nname.GT.9) goto 2058
      NAME=Mp1(Nname)
      JNAME=1
 2050 WRITE (*,1602)
 1602 FoRMAT('    BBEÄÈTE HÎMEP 1-É TEËEÃPAMMÛ')
      CALL vvodi('   -->',NTlg0(KolCTz))
      IF(NTlg0(KolCTz).EQ.KyX) Go To 1000
  205 WRITE (*,1603)
 1603 FoRMAT(/'    ÇAÄAHÈE BCE (0) ÈËÈ HET (1) ?')
      CALL vvodi('    --> ',K)
      IF(K.EQ.KyX) Go To 10
      IF(K.EQ.0) Go To 204
      IF(K.NE.1) Go To 205
      IF(KolCTz.LT.5) Go To 206
      WRITE (*,1604)
 1604 FoRMAT(/'    C MEHß, ÎÄHAKÎ, ÄÎBÎËÜHÎ ...')
      Go To 204
  206 KolCTz=KolCTz+1
      Go To 207
  204 WRITE (*,2041)
 2041 FoRMAT(/'    BEPHÎ (0), ÏPÎBEPKA (1), ÇAÏÈCÜ (2),',
     *	  ' ÈHA×E (3)')
      CALL vvodi('    --> ',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.LT.0.oR.K.GT.3) Go To 204
      L=K+1
      Go To (2110,2042,210,202),L
 2040 CALL RESTMA(NAchzoH,KPAb,DVPACp,KpEchf,KeKz,Klzf,KBCp,Klpar,
     *	     4,5,KBPP,KBPB,1996)
      Go To 220
 2042 WRITE (*,1605) NzPC
 1605 FoRMAT('    BBEÄEHÎ:'//
     * '        BAPÈAHT ',I3//
     * '     N Ï/Ï  ÔÎPMA    1-É BÈTÎK   ÏÎPÖÈß  ',
     * ' N 1-É TËÃ  ÏÎÄÏÈCÜ')
      Do 208 I=1,KolCTz
      IF(ABS(foPMA(I)-514.d0).LT.0.5.oR.
     *	       ABS(foPMA(I)-524.).LT.0.5) Go To 2055
      WRITE (*,1606)I,foPMA(I),NHAchB(I),NpoPts(I),NTlg0(I)
 1606 FoRMAT(I8,F9.1,I10,I9,I10)
      Go To 208
 2055 WRITE(*,2056)I,foPMA(I),NHAchB(I),NpoPts(I),NTlg0(I),NAME
 2056 FoRMAT(I8,F9.1,I10,I9,I10,7X,a9)
  208 CoNTINUE
      Go To 204
  210 CALL vvodi('   HÎMEP ÎÁËACTÈ (1-6) --> ',Nobl)
      IF(Nobl.EQ.KyX) Go To 1000
      IH=360+30*(Nobl-1)-1
      IF(Nobl.GT.6.oR.Nobl.LT.1) Go To 210
      CALL RETAPE(Al,1024,4,5,NAchzoH)
      Al(IH+1)=NzPC
c      Al(IH+2)=Ndz
c      Al(IH+3)=NMz
c      Al(IH+4)=Ngz
c      Al(IH+5)=NHy
c      Al(IH+6)=Nsh
c      Al(IH+7)=Nbb
      Al(IH+8)=KolCTz
      Do 263 I=1,KolCTz
      L=IH+4*(I-1)+8
      Al(L+1)=foPMA(I)
      Al(L+2)=NHAchB(I)
      Al(L+3)=NpoPts(I)
  263 Al(L+4)=NTlg0(I)
      Al(IH+29)=Nname
      CALL WRTAPE(Al,1024,4,5,NAchzoH)
      WRITE (*,532)
  532 FoRMAT(/'    +++ ÏPÎØËA ÇAÏÈCÜ B APXÈB KPC +++')
      Go To 204
 2110 NpPHAch=100000
      NpPKoH=0
      Do 212 I=1,KolCTz
      IF(NHAchB(I).LT.NpPHAch) NpPHAch=NHAchB(I)
      L=NpoPts(I)
      IF(NpoPts(I).LT.0) L=-NpoPts(I)*KBCyT
      NpoCl=NHAchB(I)+L
      IF(NpoCl.GT.NpPKoH) NpPKoH=NpoCl
  212 CoNTINUE
      NpPog=NpPKoH-NpPHAch+10
      IF(NpPog.LE.200) Go To 213
      WRITE (*,1609)
 1609 FoRMAT(///'    BHÈMAHÈE, HÓÆEH CËÈØKÎM ÄËÈHHÛÉ',
     *	' ÏPÎÃHÎÇ !!!'/'         CKÎPPEKTÈPÓÉTE ÇAÄAHÈE !'/)
      Go To 200
  213 WRITE (*,1610)
 1610 FoRMAT(/'    ÏPÎÃHÎÇ C×ÈTATÜ (0) ÈËÈ ÁPATÜ ÃÎTÎBÛÉ (1) ?')
      CALL vvodi('    --> ',KEpPog)
      IF(KEpPog.EQ.KyX) Go To 1000
      IF(KEpPog.NE.1) Go To 214
      IF(KlgpP.NE.0) Go To 215
      WRITE (*,2157)
 2157 FoRMAT(/'        ÄA HE C×ÈTAËÈ BÛ EÙE ÏPÎÃHÎÇ !!!')
      Go To 213
  214 IF(KEpPog.NE.0) Go To 213
      KBBHy=1
      Go To 82
  215 KgAPM=1
      IF(NB.LE.NpPHAch) Go To 2150
      WRITE (*,2151)
 2151 FoRMAT(/'      BHÈMAHÈE, HÎMEP BÈTKA HÓ > 1-ÃÎ BÈTKA C×ETA !'/)
      Go To (10,200,7000),KPAb
 2150 HoMHy=10*NHy+Nbb
      IF(KPAb.EQ.3) go to 1123
      call VIDTMA(NAchzoH,GApol,Gbo,Nobi,Ndi,NMi,Ngi,DVPACp,
     *	    Propellant_Value,KBid,XPid)
      
      go to 1122
 1123 continue
      Call VID615(NAchzoH,GApol,Gbo,Nobi,Ndi,NMi,Ngi,
     *		DVPACp,KBid,XPid)
 1122 Go To 2040
  220 CoNTINUE
  600 Go To 601
  800 continue
      CALL SMAf(Nz0,Kbmax)
      Go To 200
  900 continue
c manager of writing to DB
c      call write_frm_ora
	isys=SYSTEM("StDB.exe") 
      Go To 200
  920 WRITE (*,921)
  921 FoRMAT(/'    ×ÈCTÈTÜ APXÈB ÔÈÇÈKÈ (1), HET (0) ?')
      CALL vvodi('    --> ',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.NE.1) Go To 200
      CALL chiCAf(Nz0,KBMAX)
      Go To 200
  950 MHAchB=NHAchB(1)
      MpoPts=NpoPts(1)
      CALL BRF(MHAchB,MpoPts,NzPC,NHy,Nsh,Nbb,KbC,NAchzoH,
     *	    KPAb)
      Go To 200
  100 WRITE (*,8)
    8 FoRMAT(/20X,
     * ' * * *	   Ï P Î Ã H Î Ç      * * *')
   82 CALL VVoNU(NAchzoH,Nob,NHy,Nsh,Nbb,NchP,NMP,NgP,NB,
     *	   Nch,NM,Ng,THy,Hy,SoPb,KBHy,XPHy)
   21 FoRMAT(/'    ÏPÎBEPKA HÓÆHA (1), HET (0), ÈHA×E (2)')
  500 FoRMAT(/'    KATAËÎÃ HÓÆEH (1), HET (0) ?')
  512 FoRMAT('    BCE (0), EÙE (1), TAÁË (2) ?')
  514 FoRMAT('    ÇAÏÈCÛBATÜ B APXÈB (1), HET (0) ?')
      CALL VVIDP(NAchzoH,F,F81,AP)
   51 CALL vrem(THy,Nche,NMe,NC,NTC)
      CEK=1.d0*NC+0.001d0*NTC
      write(72,9801) F,F81,AP,SoPb,MshHy(1),Nob,NHy,Nsh,
     * Nbb,NB,Nch,NM,Ng,Nche,NMe,CEK,THy,MshHy(2),(Hy(JJ),JJ=1,6)
 9801 FoRMAT(/,5X,' ***  C A Ä È K  ***   ',/'F=',F6.1,
     *	'  F81=',F6.1,'	AP=',F5.1,'  SÎPÁ=',F7.5//A/
     * I3,I5,'.',I2,'.',I1,I6,2x,I2.2'.'I2.2'.'2I4':'I2,
     * ':',F6.3,' (',F9.3,')'//a/3F9.3,3F11.5)
      dblS=SoPb
      IF(KBBHy.EQ.1) Go To 215
      KgAPM=1
      WRITE (*,31)
   31 FoRMAT(/
     *'    C×ÈTATÜ ÏPÎÃHÎÇ HA ÇAÄAHHÎE K-BÎ BÈTKÎB       (1)'/
     *'    ÈËÈ C ÇAÄAHHÎÃÎ BÈTKA HA ÇAÄAHHÎE K-BÎ BÈTKÎB (2)'/
     *'    ÈËÈ C MÎÄEËÈPÎBAHÈEM MAHEBPÎB                 (3)')
      CALL vvodi('   -->',KpP)
      IF(KpP.EQ.3) Go To 5301
      IF(KpP.EQ.KyX) Go To 1000
      IF(KpP.NE.1) Go To 52
   34 WRITE (*,32)
   32 FoRMAT(/'    BBEÄÈTE KÎËÈ×ECTBÎ BÈTKÎB ÏPÎÃHÎÇA ( <= 200 )')
      CALL vvodi('   N = ',N)
      IF(N.EQ.KyX) Go To 1000
   35  WRITE (*,33)
   33 FoRMAT('    BEPHÎ (0), EÙE PAÇ (1)')
      CALL vvodi('    --> ',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.EQ.0) Go To 53
      IF(K.EQ.1) Go To 34
      Go To 35
   52 WRITE (*,36)
   36 FoRMAT(/'    ÏPÎÃHÎÇ C×ÈTATÜ C BÈTKA')
      CALL vvodi('   N = ',N)
      IF(N.EQ.KyX) Go To 1000
      WRITE (*,37)
   37 FoRMAT('    KÎËÈ×ECTBÎ BÈTKÎB ÏPÎÃHÎÇA ( <= 200 )')
      CALL vvodi('   DN = ',N1)
   39 WRITE (*,38)
   38 FoRMAT('    BEPHÎ (0), EÙE PAÇ (1)')
      CALL vvodi('    --> ',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.EQ.0) Go To 53
      IF(K.EQ.1) Go To 52
      Go To 39
 5301 N=1
   53 WRITE (*,40)
   40 FoRMAT(/'    ÏÎKAÇÛBATÜ XÎÄ ÏPÎÃHÎÇA (1) ÈËÈ HET (0) ?')
      CALL vvodi('    --> ',KBud)
      IF(KBud.EQ.KyX) Go To 1000
      WRITE (*,7300)
 7300 FoRMAT(/'      ÈÄTÈ (1), ÄÎÏÎËHÈTEËÜHÛE PEÆÈMÛ (0) ?')
      CALL vvodi('    --> ',JM)
      IF(JM.EQ.1) Go To 7901
      IF(JM.NE.0) Go To 1000
      WRITE (*,7902)
 7902 FoRMAT(/'    C PAC×ETÎM ÇÎH BÈÄÈMÎCTÈ	   (1)'/
     *	'    C PAC×ETÎM "ÖÓ" HA KAÆÄÎM BÈTKE (2)'/)
      CALL vvodi('    --> ',JM)
      IF(JM.EQ.2) NKoH=9999
      IF(JM.EQ.1) NKoH=8888
      IF(JM.LT.0.AND.JM.GT.2) Go To 1000
 7901 KSoPb=0
      WRITE (*,41)
   41 FoRMAT(/'    *** ÈÄET PAC×ET ÏPÎÃHÎÇA ***'/)
      Kid=1
      KHy=1
      NB1=NB
      Nch1=Nch
      NM1=NM
      Ng1=Ng
      SoPb=dblS
c--- for initial altitude < 160 km ---
      call vysota(Hy,HNU)
      if(HNU.GE.160.d0) go to 7905
      call akpr(HNU,aknu,HNU)
      SoPb=SoPb/aknu
c-------------------------------------
 7905 KdB=0
      CALL PROGN(NB1,Nch1,NM1,Ng1,THy,Hy,N,N1,KpP,KBud,F,F81,
     *	   AP,Kd,NKoH,No520,NHy,Nsh,Nbb,Nob)
      IF(KpP.NE.3) Go To 4100
      XPHy(8)=NB1
      XPHy(9)=Nch1
      XPHy(10)=NM1
      XPHy(11)=Ng1
      XPHy(12)=THy
      Do 4101 I=1,6
 4101 XPHy(I+12)=Hy(I)
 4100 KlgpP=1
      MKBiT(JKBiT)=NKoH
      IF(JKBiT.LT.10) JKBiT=JKBiT+1
      IF(Kd.EQ.0) Go To 60
      WRITE (*,61)(PEz(201,I),I=1,5)
   61 FoRMAT(/'    >*< BÛ ÏÛTAËÈCÜ C×ÈTATÜ ÏPÎÃHÎÇ ÄAËÜØE,×EM',
     *	  ' ÝTÎ BÎÇMÎÆHÎ >*<'/'       ÏÎCËEÄHÈÉ BÈTÎK ',F6.0,'(',
     *	F3.0,')   ',F3.0,'.',F3.0,'.',F5.0)
   60 WRITE (*,62)
   62 FoRMAT(/'    BÛÄABATÜ ÏPÎÃHÎÇ: HA ÝKPAH',14X,'(1)'/
     * 18X,'    Â ËÈÑÒÈÍÃ',13X,'(2)'/18X,'    B TEKÓÙÈÅ HÓ',10X,'(3)'/
     * 18X,'    KÎHEÖ ÇAÄA×È ÏPÎÃHÎÇA (0)')
      CALL vvodi('    --> ',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.EQ.0) Go To 1000
      IF(K.GE.1.AND.K.LE.3) Go To 67
      Go To 60
   67 WRITE (*,64)
   64 FoRMAT(/'    ÂÛÄATÜ C BÈTKA HÎMEP (BBEÄÈTE)')
      CALL vvodi('    --> ',NHAch)
      IF(NHAch.EQ.KyX) Go To 1000
      JHAch=0
      R=NHAch
      Do 65 I=1,201
      IF(ABS(PEz(I,1)-R).GT.0.00001d0) Go To 65
      IHAch=I
      JHAch=1
c Orbit has been found
      goto 966
   65 CoNTINUE
      WRITE (*,68)
   68 FoRMAT(/'    --- ÄËß ÝTÎÃÎ BÈTKA ÄAHHÛX HET ---')
      Go To 67
  966 IF(K.NE.3) Go To 66
      XPHy(8)=PEz(IHAch,1)
      XPHy(9)=PEz(IHAch,3)
      XPHy(10)=PEz(IHAch,4)
      XPHy(11)=PEz(IHAch,5)
      XPHy(12)=PEz(IHAch,6)
      Do 967 I=1,6
  967 XPHy(I+12)=PEz(IHAch,I+8)
      WRITE (*,968)NHAch
  968 FoRMAT(//'    HÓ BÈTKA ',I5,' ÏEPEÏÈCAHÛ B TEKÓÙÈE',
     *	  ' HÓ ÏPÎÃHÎÇA '/)
      Go To 60
   66 WRITE (*,69)
   69 FoRMAT(/'    HA CKÎËÜKÎ BÈTKÎB BÛÄATÜ (BBEÄÈTE)')
      CALL vvodi('   -->',NBud)
      IF(NBud.EQ.KyX) Go To 1000
      J=IHAch+NBud-1
      NKM=1
      Do 87 I=1,10
      IF(MKBiT(I).GT.NKM) NKM=MKBiT(I)
   87 CoNTINUE
      IF(J.LE.NKM) Go To 70
      L=NKM-IHAch+1
      WRITE (*,71)L,PEz(NKoH,1)
   71 FoRMAT(/'    ×EÃÎ ÇAXÎTEËÈ, Ó MEHß CTÎËÜKÎ HETÓ.'/
     *	'    MÎÃÓ BÛÄATÜ ',I3,' BÈTKÎB ÏÎ ',F5.0,'-É BKËÞ×ÈTEËÜHÎ')
      Go To 66
   70 Do 72 M=IHAch,J
   72 CALL VydPR1(M,K)
      Go To 60
 7000 WRITE (*,7001)
      ASSIGN 7020 To METob
 7001 FoRMAT(/5X,'    * CÏÓCK ÏÐÎÃÐÅÑÑ Ì *'//
     * '    BÛÁÈPAÉTE: ÔÈÇÈKA              (1)'/
     *	      11X,'    ÔÎPMÛ               (2)'/
     *        11X,'    APXÈB ÔÈÇÈKÈ È ÔÎÐÌ (3)'/
     *	      11X,'    ÇÀÏÈÑÜ Â ÁÄ         (4)'/
     *        11X,'    B Û X Î Ä           (0)')
      CALL vvodi('   -->',Kfiz)
      IF(Kfiz.EQ.KyX) Go To 1000
      IF(Kfiz.LT.0.oR.Kfiz.GT.4) Go To 7000
      Kfiz1=Kfiz+1
      Go To (1000,7010,7500,7700,7600),Kfiz1
 7010 WRITE (*,7011)
 7011 FoRMAT(/'    BBEÄÈTE ÇAÄAHÈE HA PAC×ET :'/)
      CALL vvodi('   HÎMEP BAPÈAHTA',NzPC)
      CALL vvodi('   HÎMEP BÈTKA C×ETA',NHAchB(1))
      WRITE (*,28)
   28 FoRMAT(/'    BEPHÎ (0), HET (1) ?')
      CALL vvodi('   -->',L)
      IF(L.EQ.KyX) Go To 1000
      IF(L.NE.0) Go To 7010
      NpPHAch=NHAchB(1)
      NpPog=5
      Go To 213
 7020 GA0=GApol
      IF(NKPA.NE.4) Go To 7910
      Do 7911 I=1,3
      C(I+8)=XPHy(I+12)
      C(I+11)=XPHy(I+15)
 7911 C(I+2)=XPHy(I+8)
      C(6)=XPHy(12)
      C(1)=XPHy(8)
      Go To 7913
 7910 IB=1
 7023 IF(NHAchB(1).EQ.nint(PEz(IB,1))) Go To 7021
      IF(IB.LT.200) Go To 7022
      WRITE (*,6141)NHAchB(1)
      Go To 7000
 7022 IB=IB+1
      Go To 7023
 7021 Do 7024 I=1,17
 7024 C(I)=PEz(IB,I)
 7913 NMEC=C(4)-0.999
      KbC=1     
      CALL KP615(C,DVPACp)
      ygdAl=0.
      obE=Nobi
      NTTPAC(2)=20
      L=NTTPAC(1)-20
      Do 3789 I=1,20
      Do 3789 J=1,10
 3789 TPCPuB(I,J)=TPAC(L+I,J)
      Nd9=nint(C(3))
      NM9=nint(C(4))
      Ng9=nint(C(5))
      IF(Klzf.NE.0) CALL zpAPXf(Nz0,KBMAX,KoT,obE,NzPC,Nd9,NM9,
     *			     Ng9,NHy,Nsh,Nbb,IB,GApol,Gbo,DVPACp,
     *			    ygdAl,ATlg,0.d0,0.d0)

c store NU of burn start and end
      Nz502=NAchzoH+11
      CALL RETAPE(Al,1024,4,5,Nz502)
      Al(250)=Nob
      Al(251)=NHy
      Al(252)=Nsh
      Al(253)=Nbb
      Al(257)=C(1)
      Do 3790 I=1,3
 3790 Al(257+I)=C(I+2)
      Al(268)=SoPb
      Do 3791 I=1,20
 3791 Al(269+I)=Al(249+I)
      Do 3792 I=1,2
      Do 3792 J=1,7
      IH=260+20*(I-1)
 3792 Al(IH+J)=eTAp(I,J)
c form and write NU of burn start & end to file
      call formnu(Al(250),1)
      call formnu(Al(270),2)
      Go To 7000
 7500 continue
      MHAchB=NHAchB(1)
      MpoPts=1
      CALL BRF(MHAchB,MpoPts,NzPC,NHy,Nsh,Nbb,KbC,NAchzoH,KPAb)
      Go To 7000
 7600 continue
c manager of writing to DB for Progress
 7605 write(*,7610)
 7610 format(/'    ÇÀÏÈÑÜ ÔÎÐÌ (1)'/
     *        '    ÇÀÏÈÑÜ ÍÓ   (2)'/
     *        '    ÂÛÕÎÄ       (0)')
      call vvodi('   ',kwr)
      select case(kwr)
        case(1)
c        call write_frm_ora
	isys=SYSTEM("StDB.exe")
        case(2)
        call write_nu_ora
c	isys=SYSTEM("NUPI.exe")
      end select
      if(kwr.ne.0) goto 7605
      Go To 7000
 7700 continue
      CALL SMAf(Nz0,Kbmax)
      Go To 7000
 3500 kgapm=1
      CALL oTNoS
      Go To 1000

C determination of ballistic coefficient
 3600 CALL Sopred
         goto 1000
C end of task                   

  601 DVT1=DV1*1000.d0
      IF(KPAb.EQ.3) Go To 6010
      write(72,9802) Mshid(1),GApol,Gbo,GCA,Tag1,ydTag1,DVT1,
     * Mshid(2),XT,yT,SCA,
     * Mshid(3),ALb,Ndi,NMi,Ngi,Tag2,ydTag2,DVPACp
 9802 FoRMAT(//A/F7.1,2F8.1,3F7.1,//a/2F9.5,F11.5,//a/6F6.1,
     *	I5,'.',I2,'.',I4//25X,'P ÁT  P ÓÄ ÁT DVPACÏ'/24X,
     *	 F6.1,2F7.1)
      Go To 6020
 6010 write(72,6011) Mid615,GApol,GCA,Tag1,ydTag1,DVT1,Ndi,NMi,Ngi,
     *	Tag2,ydTag2,DVPACp
 6011 FoRMAT(/A/F7.1,F7.1,F10.1,2F7.1,I5,'.',I2,'.',I4//
     * 8X,'P ÁT  P ÓÄ ÁT DVPACÏ'/5X,F6.1,2F8.1)
 6020 WRITE (*,602)
 602  FoRMAT(/'    B C×ET (1) ÈËÈ HA BÛXÎÄ (0) ?')
      CALL vvodi(   '-->',K)
      IF(K.EQ.KyX) Go To 1000
      IF(K.EQ.0) Go To 10
      IF(K.NE.1) Go To 601

c output NU, ID ,MODES and TASK to file for printing     
       Call pr_rez(NAchzoH,KPAb,DVPACp,KpEchf,KeKz,Klzf,KBCp,Klpl,
     *             4,5,KBPP,KBPB,1996,XPid,
     *             NzPC,KolCTz,foPMA,NHAchB,NpoPts,NTlg0,NAME)
     
      IF(NKPA.EQ.4) Go To METob,(6066,7020)
      IF(KEpPog.EQ.0) Go To 605
      Go To 6060
  605 WRITE (*,41)
      NB1=NB
      NM1=NM
      Nch1=Nch
      Ng1=Ng
      SoPb=dblS
      KSoPb=1
      KdB=0
      CALL PROGN(NB1,Nch1,NM1,Ng1,THy,Hy,NpPHAch,NpPog,2,0,
     *	  F,F81,AP,Kd,NKoH,No520,NHy,Nsh,Nbb,Nob)
      KlgpP=1
 6060 WRITE (*,606)
  606 FoRMAT(/'    >*< ÏPÎÃHÎÇ ÃÎTÎB, C×ÈTAÞ CÏÓCK >*<'/)
      Go To METob,(6066,7020)
 6066 KfoPM=0
      Kf14=0
      Kf512=0
c open file to store names of forms
      open(10,file='forms/status')
      HoMHy=10*NHy+Nbb
      Bdy=KBub1-1
c      BoP=10*(KoP1-1)+KCTAb1
c      bop=1.d0
c      if(kop1.eq.2.and.kctab1.eq.1) bop=2.d0
c      if(kop1.eq.1.and.kctab1.eq.2) bop=3.d0
c      if(kop1.eq.2.and.kctab1.eq.2) bop=4.d0
      TK14=86400.-PEz(3,6)+PEz(2,6)
      IF(PEz(2,6).GT.43200.d0.AND.PEz(3,6).LT.43200.d0)
     *			   TK14=PEz(2,6)-PEz(3,6)
      ToPb=86400.d0-TK14
      Dle1=PEz(3,7)-PEz(2,7)
      IF(PEz(3,7).GT.0.d0.AND.PEz(2,7).LE.0.d0) Dle1=-360.d0+Dle1
      DleKB=ABS(Dle1)
      le1=-55.d0+DleKB
      KoT=0
c calculation of forms      
      Do 5000 LK=1,KolCTz
      KlDTB=0
      Kolf=0
      KfoPM=foPMA(LK)+0.1d0
      Kf514=0
      IF(KfoPM.EQ.514.oR.KfoPM.EQ.524) Kf514=1
      IF(KfoPM.EQ.514.oR.KfoPM.EQ.524) KfoPM=foPMA(LK)*10+0.1d0
      KfoPM1=KfoPM*0.1
      MTf='   '
      IF(KfoPM.EQ.5141.oR.KfoPM.EQ.5241) MTf='-ÁC'
      IF(KfoPM.EQ.5142.oR.KfoPM.EQ.5242) MTf='-ÓC'
      WRITE (*,5566) nint(foPMA(LK)),MTf
 5566 FoRMAT(/'        * ÔÎPMA ',i4,A3,' *'/)
      MbC=0
      IF(KfoPM.NE.14.AND.
     *	 KfoPM.NE.5141.AND.KfoPM.NE.5241) Go To 610
      KbC=1
      GA0=GApol-Gbo*(1-Kbob)
      MbC=1
  610 IF(KfoPM.NE.511.AND.KfoPM.NE.522.AND.KfoPM.NE.521.AND.
     *	 KfoPM.NE.5142.AND.KfoPM.NE.5242.and.kfopm.ne.510) Go To 611
      KbC=0
      GA0=GApol-Gbo*(1-Kboy)
      MbC=1
  611 IF(KfoPM.NE.0) Go To 1111
      MbC=1
      GA0=GApol-Gbo*((1-Kbob)*KbC+(1-Kboy)*(1-KbC))
 1111 IF(MbC.EQ.1) Go To 612
      WRITE (*,609)LK
  609 FoRMAT(/'    B H È M A H È E , CTPÎKA ',I2,
     *	      ' HE ÎÁPAÁATÛBAETCß !')
      Go To 5000
  612 NHAch=NHAchB(LK)
      KgoTB=0
      KgoTd=0
      KBf=0
c      Tlg=NTlg0(LK)+100*Nsh
      Tlg=NTlg0(LK)
      obE=Nobi
  618 IB=1
  614 NBpP=nint(PEz(IB,1))
      IF(NHAch.EQ.NBpP) Go To 613
      IF(IB.LT.200) Go To 6140
      WRITE (*,6141)NHAch
 6141 FoRMAT(/'    HET ÏPÎÃHÎÇA ÄËß BÈTKA ',I5)
      Go To 5000
 6140 IB=IB+1
      Go To 614
  613 IF(KfoPM.EQ.14.oR.
     *	 KfoPM.EQ.0) Go To 615
      IF(KfoPM.NE.5141.AND.KfoPM.NE.5241) Go To 616
      IF(PEz(IB,7).LE.104..AND.PEz(IB,7).GE.-123.d0) Go To 615
  617 NHAch=NHAch+1
      Go To 618
  616 IF(kfopm.ne.510.and.KfoPM.NE.511.AND.KfoPM.NE.522.AND.
     *   KfoPM.NE.521.AND.
     *	 KfoPM.NE.5142.AND.KfoPM.NE.5242) Go To 615
      IF(PEz(IB,7).LE.20.d0.AND.PEz(IB,7).GE.-55.d0) Go To 615
      Go To 617
  615 Do 619 I=1,17
  619 C(I)=PEz(IB,I)
      NMEC=C(4)-0.999d0
      if(KfoPM.EQ.522) k522=2      
      if(KfoPM.EQ.521.or.kfopm.eq.510) k522=1      
C recalculation to abcolute CS for f522      
      Do i=1,6
         Ya(I)=C(I+8)
      EndDo
      Ya(4)=Ya(4)-OMZ*Ya(2)
      Ya(5)=Ya(5)+OMZ*Ya(1)
c++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      CALL kpTMA(C,KBCp)
c++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      IF(ABS(C(17)-100.d0).LT.0.0001d0) Go To 200
      KgoTB=KgoTB+1
      CALL ygld(ygdAl)
      IF(KfoPM1.NE.524) Go To 3100
      IF(KBf.NE.0) Go To 3101
      TeK1=PEz(IB,6)
      leK1=PEz(IB,7)
      IF(leK1.LT.0.) leK1=360.d0+leK1
      CALL gPMiH(leK1)
      dBiT1=PEz(IB,3)
      BiT1M=PEz(IB,4)
c	gBiT1=PEz(IB,5)-1900.d0
      gBiT1=PEz(IB,5)
 3101 KBf=KBf+1
      CALL Azp(PEz(IB,9),PEz(IB,10),PEz(IB,12),PEz(IB,13),
     *	 PEz(IB,14),PEz(IB,7),PEz(IB,6),eTAp(10,1),lg,CyTB(KBf))
      CALL gPMiH(CyTB(KBf))
      BiT(KBf)=PEz(IB,1)
      TBKf(KBf)=eTAp(10,1)
      fpoC(KBf)=fg
      lpoC(KBf)=lg
      IF(lg.LT.0.) lpoC(KBf)=360.d0+lg
      CALL gPMiH(fpoC(KBf))
      CALL gPMiH(lpoC(KBf))
      IF(KfoPM.NE.5242) Go To 622
      Do 3102 I=1,6
 3102 C(I)=eTAp(11,I+1)
      CALL sirdol(C,fCP,lCP)
      fpCP(KBf)=fCP*pPg
      lpCP(KBf)=lCP*pPg
      CALL Azp(PEz(IB,9),PEz(IB,10),PEz(IB,12),PEz(IB,13),
     *PEz(IB,14),PEz(IB,7),PEz(IB,6),eTAp(11,1),lpCP(KBf),ApCP(KBf))
      CALL gPMiH(ApCP(KBf))
      CALL gPMiH(fpCP(KBf))
      IF(lpCP(KBf).LT.0.) lpCP(KBf)=360.+lpCP(KBf)
	CALL gPMiH(lpCP(KBf))
      TpCP(KBf)=eTAp(11,1)
      TKPEH(KBf)=SKPEH
      Go To 622
 3100 IF(KfoPM1.NE.514) Go To 7301
c====  form 514 ===
      IUS=1-KbC
      CALL foP514(IUS,NAME,HoMHy,obE,Tlg,C(1),C(3),C(4),C(5),
     *	     SKPEH,PEz(IB,6),PEz(IB,8),PEz(IB,7))
      Tlg=Tlg+1
      Go To 622
 7301 IF(KfoPM.NE.511) Go To 6221
c==== form 511 ==========================
      Do 870 I=1,6
  870 BiT(I)=eTAp(5,I+1)
      CALL sirdol(BiT,fP25,lP25)
      l25=lP25*pPg
      CALL TPyg(BiT,1,4,TET25)
      TET25=TET25*pPg
      TBK=eTAp(1,1)
      IF(TBK.LT.0.d0) TBK=TBK+86400.d0
      call TVKTMA(TBK,TBKokr,klzf)
      Ats=ABS(KtsiKl-1)
      DTAyf=DTAy
      IF(KtsiKl.EQ.1) DTAyf=0.d0
      DTPf=DTPAzd
      IF(KtsiKl.EQ.0) DTPf=0.d0
      ToCp=eTAp(10,1)
      IF(ToCp.GT.86400.d0) ToCp=ToCp-86400.d0
      CALL THBL(eTAp,11,10,10,Mch,MM,ACEK,Ho,fo,lo)
c     god=C(5)-1900.d0
      lef=C(7)
      IF(lef.LT.0.d0) lef=lef+360.d0
      Nobl=KgoTB
        if(KBub1.eq.2) then
           V1Cyd=0.0
           T1Cyd=0.0
        endif
      bopp=bop+10.d0*(kyc-1)
      if(kyc.eq.1) go to 9001
      deltt=0.d0
      dk=0.d0
      dt0=0.d0
c---------------------------------------------------------------------
 9001 ccc=dv1*1000.d0
      V2c=ccc-5.d0
      t2c=tdy1/ccc*V2c
      call F511
     *(HoMHy,obE,Tlg,
     * C(1),C(2),C(3),C(4),C(5),PEz(IB,6),lef,
     * DVT1,Tdy1,KBub1,kop,KCTAb,kboy,kyc,KtsiKl,
     * TBKokr,P1,G1,TET1,
     * V1Cyd,T1Cyd,V2c,t2c,
     * DTPf,DTAyf,TH104,
     * etap(5,1),L25,TET25,
     * DTvn,aNaus,SKPEH,VSR,aKaus,aYt,
     * TC,AKPyC0,ANPyC,
     * ygdAl,Tocp,fo,lo)
     
c---------------------------------------------------------------------
      Tlg=Tlg+1
      KfoPM=511
      K=8888
      le1=-55.+ABS(PEz(IB+1,7)-PEz(IB,7))
      IF(KgoTB.EQ.NpoPts(LK)) K=9999
      NpoPts1=NpoPts(LK)+1
      IF(NpoPts(LK).LT.0.AND.KgoTd.EQ.NpoPts1.AND.C(7).LT.le1) K=9999
      I1=Nz512C
      I2=Nz512
      IF(Nobl.LT.13) Go To 911
      Nobl=KgoTB-12
      I1=Nz512C+1
      I2=Nz512+1
  911 continue
      Kolf=Kolf+1
      CALL RETAPE(Al,1024,4,5,Nz512)
      Al(1024)=Kolf
      CALL WRTAPE(Al,1024,4,5,Nz512)

c write settings to archive for 3 or 4 first orbits (only for SKD)
c      if(KBub1.eq.1.and.
c     * (Kolf.le.3.or.Kolf.eq.4.and.nint(C(2)).eq.4))
c     * CALL wrust(NAchzoH,TBK,DTAyf,DTPf,SKPEH,DELTT,DK,DT0,TC,
c     *	    ANPyC,AKPyC0,lpPits,HPAzd,nint(C(1)),nint(C(2)))

      Go To 622
 6221 if(KfoPM.eq.522.or.KfoPM.eq.521.or.kfopm.eq.510) then

      if(KfoPM.eq.521.or.kfopm.eq.510) then
        DVmax=.128
        Altmax=460.
      endif

      if(KfoPM.eq.522) then
        DVmax=.1152
        Altmax=420.
      endif

c Calculatuion of weight setting - Cn
c Gcorr is weight corrected using real DPO thrust (XPid(16))

      if(KfoPM.eq.521.or.kfopm.eq.510) Gcorr=51.67*GA0/XPid(16)
      if(KfoPM.eq.522) Gcorr=GA0
      
      Coeff_Weigt=1.0
      if(Kboy.eq.0) Coeff_Weigt=1+1324.044/Gcorr
      Cn=Gcorr*Coeff_Weigt+Propellant_Value

c Calculatuion of "recalculated" altitude - Altitude_On ( 2 values !!!)
      Call A01(Ya(1),Ya(2),Ya(3),Ya(4),Ya(5),Ya(6),Zagl(1),
     <         Zagl(2),Zagl(3),Zagl(4),Zagl(5),Zagl(6),Hmin,Hmax)

      Altitude_Mean=(Hmin+Hmax)/2.
      if(KBub1.eq.2) then               ! "pure" DPO !
        Delta_Altitude=(Enangle512+1.15)*95.
         if(abs(Delta_Altitude).GE.20.) then
             Delta_Altitude=sign(20.,Delta_Altitude)
         endif
            Coeff_x=1.7-.58*(DVtorm-.0896)/(DVmax-.0896)    
        Altitude_On=(Altitude_Mean+Delta_Altitude)*Coeff_x
        if(Altitude_On.LE.350.) Altitude_On=350.
        if(Altitude_On.GE.Altmax) Altitude_On=Altmax
        do j=1,13
           DV_522(j)=0.
        enddo
                     else            ! normal mode !
        Delta_Altitude=(Enangle512+1.34)*85.
        if(abs(Delta_Altitude).GE.20.) then
             Delta_Altitude=sign(20.,Delta_Altitude)
        endif     
            Coeff_x=1.65-.65*(DVtorm-.0896)/(DVmax-.0896)    
        Altitude_On=(Altitude_Mean+Delta_Altitude)*Coeff_x
        if(Altitude_On.LE.310.) Altitude_On=310.
        if(Altitude_On.GE.Altmax) Altitude_On=Altmax
      endif

c round altitude
      Altitude_On=nint(Altitude_On*3.2768)/3.2768

c round DVi to 0.04
      do i=1,knumber
         DV_522(i)=0.04*nint(DV_522(i)/0.04)
      enddo

      if(KBub1.eq.2) then  ! for "pure" DPO !
c         V1Cyd=0.
         De=0.
      else                 ! normal mode !
c calculation of setting - De
      Delta_DV_min=abs(abs(DV_522(2))-abs(DV_522(1)))
      do i=2,knumber
        Delta_DV=abs(abs(DV_522(i+1))-abs(DV_522(i)))
	if(Delta_DV.lt.Delta_DV_min) then
	      Delta_DV_min=Delta_DV
	endif      
      enddo
      De=abs(Delta_DV_min)-0.12
      if(De.lt.0.04) De=0.04
      
c  fill rest of array DV_522
      do i=knumber+2,kmax
	  DV_522(i)=De*2**(i-knumber-1)
      enddo
      endif

      lef=C(7)
      IF(lef.LT.0.) lef=lef+360.
      TBK=eTAp(1,1)
      IF(TBK.LT.0.) TBK=TBK+86400.
      
      call TVKTMA(TBK,TBKokr,klzf)

c  calculation of form 522
      if(KfoPM.eq.522) call f522
     *(HoMHy,obE,Tlg,C(1),C(3),C(4),C(5),PEz(IB,6),lef,
     * TBKokr,Altitude_On,DVT1,V1Cyd,Cn,DV_522,De)

c  calculation of form 521
      if(KfoPM.eq.521) call f521
     *(HoMHy,obE,Tlg,C(1),C(3),C(4),C(5),PEz(IB,6),lef,
     * TBKokr,Altitude_On,DVT1,V1Cyd,Cn,DV_522,De)
     
     
      if(kfopm.ne.510) go to 7777 
      
      Xtsa=xt*2145.d0
      
      Do 1870 I=1,6
 1870 BiT(I)=eTAp(5,I+1)
      CALL sirdol(BiT,fP25,lP25)
      l25=lP25*pPg
      CALL TPyg(BiT,1,4,TET25)
      TET25=TET25*pPg
      TBK=eTAp(1,1)
      IF(TBK.LT.0.d0) TBK=TBK+86400.d0
      call TVKTMA(TBK,TBKokr,klzf)
      Ats=ABS(KtsiKl-1)
      DTAyf=DTAy
      IF(KtsiKl.EQ.1) DTAyf=0.d0
      DTPf=DTPAzd
      IF(KtsiKl.EQ.0) DTPf=0.d0
      ToCp=eTAp(10,1)
      IF(ToCp.GT.86400.d0) ToCp=ToCp-86400.d0
      CALL THBL(eTAp,11,10,10,Mch,MM,ACEK,Ho,fo,lo)
      lef=C(7)
      IF(lef.LT.0.d0) lef=lef+360.d0
      Nobl=KgoTB
c        if(KBub1.eq.2) then
c           V1Cyd=0.0
c           T1Cyd=0.0
c        endif
      bopp=bop+10.d0*(kyc-1)
      if(kyc.eq.1) go to 8001
      deltt=0.d0
      dk=0.d0
      dt0=0.d0
c---------------------------------------------------------------------
 8001 ccc=dv1*1000.d0
      V2c=ccc-5.d0
      t2c=tdy1/ccc*V2c
      
      call F510
     *(HoMHy,obE,Tlg,
     * C(1),C(2),C(3),C(4),C(5),PEz(IB,6),lef,
     * DVT1,Tdy1,KBub1,kop,KCTAb,kboy,kyc,KtsiKl,
     * TBKokr,P1,G1,TET1,
     * V1Cyd,T1Cyd,V2c,t2c,
     * DTPf,DTAyf,TH104,
     * etap(5,1),L25,TET25,
     * DTvn,aNaus,SKPEH,VSR,aKaus,aYt,
     * TC,AKPyC0,ANPyC,
     * ygdAl,Tocp,fo,lo,
     * Altitude_On,Cn,DV_522,De,
     * Gapol,Gbo,tag2,Xtsa)
 
 7777 Tlg=Tlg+1

      endif
      
      IF(KfoPM.NE.14) Go To 622
      IF(KBf.NE.0) Go To 625
      BeKB=PEz(IB,1)
      deKB=PEz(IB,3)
      eKBM=PEz(IB,4)
c      geKB=PEz(IB,5)-1900.d0
      geKB=PEz(IB,5)
      TeKB=PEz(IB,6)
      leKB=PEz(IB,7)
      IF(leKB.LT.0.) leKB=360.d0+leKB
  625 KBf=KBf+1
      KfoPM=14
      BiT(KBf)=C(1)
      CyTB(KBf)=PEz(IB,2)
      TBKf(KBf)=eTAp(1,1)
      IF(PEz(IB,6).LT.ToPb.AND.TBKf(KBf).GT.43200.d0) Go To 9651
      IF(TBKf(KBf).GE.PEz(IB,6)) Go To 650
 9651 BiT(KBf)=BiT(KBf)-1
      IF(CyTB(KBf).LE.1) Go To 651
      CyTB(KBf)=CyTB(KBf)-1
      Go To 650
  651 lpoP=380.d0-16.d0*ABS(PEz(IB+1,7)-PEz(IB,7))
      CyTB(KBf)=15.d0
      IF(PEz(IB,7).LT.lpoP) CyTB(KBf)=16.d0
  650 IF(TBKf(KBf).LT.0.) TBKf(KBf)=TBKf(KBf)+86400.d0
      fpoC(KBf)=fg
      IF(lg.LT.0.d0) lg=360.d0+lg
      lpoC(KBf)=lg
      ygldA(KBf)=ygdAl
      
c--- for F014M ---
      Do 7220 I=1,17
 7220 C(I)=PEz(IB,I)

      call SVET_F014M(c,sozut(kbf),sozve(kbf),
     *                  tenvh(kbf),tenvy(kbf)) 
c--------------------     
            
c  622 ATlg=Tlg-100*Nsh-1
  622 ATlg=Tlg-1
      Nd9=nint(PEz(IB,3))
      NM9=nint(PEz(IB,4))
      Ng9=nint(PEz(IB,5))
	IF(Klzf.NE.0.AND.KfoPM.NE.522.AND.KfoPM.NE.521)
     *  CALL zpAPXf(Nz0,KBMAX,
     *	  KoT,obE,NzPC,Nd9,NM9,Ng9,NHy,Nsh,Nbb,IB,GApol,
     <    Gbo,DVPACp,ygdAl,ATlg,l25,TET25)
      IF(KoT.NE.0) Go To 200
      IF(NpoPts(LK).EQ.KgoTB.AND.KfoPM.EQ.14) Go To 621
      IF(NpoPts(LK).EQ.KgoTB.AND.KfoPM.EQ.5241) Go To 3300
      IF(NpoPts(LK).EQ.KgoTB.AND.KfoPM.EQ.5242) Go To 3400
      IF(NpoPts(LK).EQ.KgoTB) Go To 5001
      IF(KfoPM.NE.5141.AND.KfoPM.NE.5241) Go To 5020
      leKBp=DleKB-123.d0
      IF(C(7).GE.leKBp) Go To 5020
      KgoTd=KgoTd-1
      IF(KfoPM.NE.5241) Go To 5020
 3300 continue
      CALL F524(NAME,KBf,HoMHy,obE,Tlg,dBiT1,BiT1M,gBiT1,
     *	   TeK1,leK1,BiT,TBKf,fpoC,lpoC,CyTB)
      IF(NpoPts(LK).GT.0) Go To 5000
      Tlg=Tlg+1
      KBf=0
 5020 IF(KfoPM.NE.511.AND.KfoPM.NE.5142.AND.kfopm.ne.510.and.
     *   KfoPM.NE.522.AND.KfoPM.NE.521.AND.KfoPM.NE.5242)
     *  Go To 910
      IF(C(7).GE.le1) Go To 910
      KgoTd=KgoTd-1
      IF(KfoPM.NE.5242) Go To 910
 3400 continue
      CALL F524U(NAME,KBf,HoMHy,obE,Tlg,dBiT1,BiT1M,gBiT1,TeK1,
     *	leK1,BiT,TBKf,fpoC,lpoC,CyTB,TKPEH,TpCP,fpCP,lpCP,ApCP)
      IF(NpoPts(LK).GT.0) Go To 5000
      Tlg=Tlg+1
      KBf=0
  910 IF(KfoPM.NE.14) Go To 620
      TK14=86400.-PEz(IB+1,6)+PEz(IB,6)
      IF(TK14.GT.86400.d0) TK14=TK14-86400.d0
      IF(PEz(IB,6).LT.TK14.oR.NpoPts(LK).GT.0) Go To 620
  621 continue
  
      CALL F14M(KBf,BiT,CyTB,TBKf,ygldA,fpoC,lpoC,HoMHy,
     *	    obE,Tlg,BeKB,deKB,eKBM,geKB,TeKB,leKB,DVT1,
     *	    Tdy1,DTAy,Bdy,BoP,sozut,sozve,tenvh,tenvy)
     
c      CALL F14(KBf,BiT,CyTB,TBKf,ygldA,fpoC,lpoC,HoMHy,
c     *	    obE,Tlg,BeKB,deKB,eKBM,geKB,TeKB,leKB,DVT1,
c     *	    Tdy1,DTAy,Bdy,BoP)
     
      Nobl=1
      IF(NpoPts(LK).LT.0) Nobl=-(KgoTd-1)
      Kolf=Kolf+1
      CALL RETAPE(Al,1024,4,5,Nz14)
      Al(1024)=Kolf
      CALL WRTAPE(Al,1024,4,5,Nz14)
      IF(NpoPts(LK).GT.0) Go To 5001
      Tlg=Tlg+1
      KgoTd=KgoTd-1
      KBf=0
  620 IF(NpoPts(LK).EQ.KgoTd) Go To 5001
      NHAch=NHAch+1
      Go To 618
 5001 IF(KfoPM.NE.511) Go To 5004
      IF(KeKz.LE.0) Go To 5004
      Ne=(KeKz-1)/2+1
      Do 5005 I=1,Ne
      L=1
 5006 N1=Nz512C
      N2=Nz512
      Nob=L
      IF(L.LT.13) Go To 5007
      Nob=L-12
      N1=Nz512C+1
      N2=Nz512+1
 5007 continue
      IF(K.EQ.9999) Go To 5008
      L=L+1
      Go To 5006
 5008 CoNTINUE
 5005 CoNTINUE
      Kf512=L
 5004 IF(KfoPM.NE.14) Go To 5000
      IF(KeKz.LE.0) Go To 5000
      N=1
      IF(NpoPts(LK).LT.0) N=ABS(NpoPts(LK))
      Kf14=N
      Do 5002 J=1,N
 5002 continue
c	CALL fprint('f14k',nz141)
      Ne=(KeKz-1)/3+1
      Do 5003 I=1,Ne
      Do 5003 J=1,N
 5003 continue
c	CALL fprint('f14',nz14)
 5000 CoNTINUE
c close file with names of forms
      close(10)
c prepare file for printing
      Call pr_file(0,0,0,0,0,0,0)
      Go To 200
C...
      END
      


      
     
     
     
     
     
        
      
      
      
