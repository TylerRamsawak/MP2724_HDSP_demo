#MP2724 by Tyler Ramsawak


class MP2724_i2c:
    def __init__(self, i2c, addr=0x3F):
        self.i2c = i2c
        self.addr = addr
    
    #read register
    def peek(self, reg):
        return self.i2c.readfrom_mem(self.addr, reg, 1)[0]
    
    #write to register
    def poke(self, reg):
        return None
    
    #extract bits from register
    def bf(self, reg, msb, lsb=None):
        data = self.peek(reg) & 0xFF
                
        if lsb is None:
            width = 1
            extracted_value = (data >> msb) & 0b1
        else:
            width = msb - lsb + 1
            mask = (1 << width) - 1
            extracted_value = (data >> lsb) & mask
        
        return f'{extracted_value:0{width}b}'
    
    
    #CHG_CTRL0
    def reg_rst(self):
        return self.bf(0x00, 7)
    
    def en_stat_ib(self):
        return self.bf(0x00, 6)
    
    def en_pg_ntc2(self):
        return self.bf(0x00, 5)
    
    def lock_chg(self):
        return self.bf(0x00, 4)
    
    def holdoff_tmr(self):
        return self.bf(0x00, 3)
    
    def sw_freq(self):
        return self.bf(0x00, 2, 1)
    
    def en_vin_trk(self):
        return self.bf(0x00, 0)
    
    #IIN
    def iin_mode(self):
        return self.bf(0x01, 7, 5)
    
    def iin_lim(self):
        return self.bf(0x01, 4, 0)
    
    #CHG_PARAMETER0
    def vpre(self):
        return self.bf(0x02, 7, 6)
    def icc(self):
        return self.bf(0x02, 5, 0)
    
    #CHG_PARAMETER1
    def ipre(self):
        return self.bf(0x03, 7, 4)
    
    def iterm(self):
        return self.bf(0x03, 3, 0)
    
    #CHG_PARAMETER2
    def vrechg(self):
        return self.bf(0x04, 7)
    
    def itrickle(self):
        return self.bf(0x04, 6, 4)
    
    def vin_lim(self):
        return self.bf(0x04, 3, 0)
    
    #CHG_PARAMETER3
    def topoff_tmr(self):
        return self.bf(0x05, 7, 6)
    
    def vbatt(self):
        return self.bf(0x05, 5, 0)
    
    #CHG_CTRL1
    def sys_min(self):
        return self.bf(0x06, 5, 3)
    
    def treg(self):
        return self.bf(0x06, 2, 0)
    
    #CHG_CTRL2
    def ib_en(self):
        return self.bf(0x07, 7)
    
    def watchdog_rst(self):
        return self.bf(0x07, 6)
    
    def watchdog(self):
        return self.bf(0x07, 5, 4)
    
    def en_term(self):
        return self.bf(0x07, 3)
    
    def en_tmr2x(self):
        return self.bf(0x07, 2)
    
    def chg_timer(self):
        return self.bf(0x07, 1, 0)
    
    #CHG_CTRL3
    def battfet_dis(self):
        return self.bf(0x08, 7)
    
    def battfet_dly(self):
        return self.bf(0x08, 6)
    
    def battfet_rst_en(self):
        return self.bf(0x08, 5)
    
    def olim(self):
        return self.bf(0x08, 4, 3)
    
    def vboost(self):
        return self.bf(0x08, 2, 0)
    
    #CHG_CTRL4
    def cc_cfg(self):
        return self.bf(0x09, 6, 4)
    
    def en_boost(self):
        return self.bf(0x09, 2)
    
    def en_buck(self):
        return self.bf(0x09, 1)
    
    def en_cng(self):
        return self.bf(0x09, 0)
    
    #VIN_DET
    def autodpm(self):
        return self.bf(0x0A, 5)
    
    def forcedpdm(self):
        return self.bf(0x0A, 4)
    
    def force_cc(self):
        return self.bf(0x0A, 1, 0)
    
    #CHG_CTRL5
    def ntc1_action(self):
        return self.bf(0x0C, 6)
    
    def ntc2_action(self):
        return self.bf(0x0C, 5)
    
    def batt_ovp_en(self):
        return self.bf(0x0C, 4)
    
    def batt_low(self):
        return self.bf(0x0C, 3, 2)
    
    def boost_stp_en(self):
        return self.bf(0x0C, 1)
    
    def boost_otp_en(self):
        return self.bf(0x0C, 0)
    
    #NTC_ACTION
    def warm_act(self):
        return self.bf(0x0D, 7, 6)
    
    def cool_act(self):
        return self.bf(0x0D, 5, 4)
    
    def jeita_vset(self):
        return self.bf(0x0D, 3, 2)
    
    def jeita_iset(self):
        return self.bf(0x0D, 1, 0)
    
    #NTC_TH
    def vhot(self):
        return self.bf(0x0E, 7, 6)
    
    def vwarm(self):
        return self.bf(0x0E, 5, 4)
    
    def vcool(self):
        return self.bf(0x0E, 3, 2)
    
    def vcold(self):
        return self.bf(0x0E, 1, 0)
    
    #VIN_IMPD
    def vin_src_en(self):
        return self.bf(0x0F, 6)
    
    def ivin_src(self):
        return self.bf(0x0F, 5, 2)
    
    def vin_test(self):
        return self.bf(0x0F, 1, 0)
    
    #INT_MASK
    def mask_therm(self):
        return self.bf(0x10, 6)
    
    def mask_dpm(self):
        return self.bf(0x10, 4)
    
    def mask_topoff(self):
        return self.bf(0x10, 3)
    
    def mask_cc_int(self):
        return self.bf(0x10, 2)
    
    def mask_batt_low(self):
        return self.bf(0x10, 1)
    
    def mask_debug(self):
        return self.bf(0x10, 0)
    
    #STATUS0
    def dpdm_stat(self):
        return self.bf(0x11, 7, 4)
    
    def vindpm_stat(self):
        return self.bf(0x11, 1)
    
    def iindpm_stat(self):
        return self.bf(0x11, 0)
    
    #STATUS1
    def vin_gd(self):
        return self.bf(0x12, 6)
    
    def vin_rdy(self):
        return self.bf(0x12, 5)
    
    def legacycable(self):
        return self.bf(0x12, 4)
    
    def therm_stat(self):
        return self.bf(0x12, 3)
    
    def vsys_stat(self):
        return self.bf(0x12, 2)
    
    def watchdog_dault(self):
        return self.bf(0x12, 1)
    
    def watchdog_bark(self):
        return self.bf(0x12, 0)
    
    #STATUS2
    def chg_stat(self):
        return self.bf(0x13, 7, 5)
    
    def boost_dault(self):
        return self.bf(0x13, 4, 2)
    
    def chg_fault(self):
        return self.bf(0x13, 1, 0)
    
    #STATUS3
    def ntc_missing(self):
        return self.bf(0x14, 7)
    
    def batt_missing(self):
        return self.bf(0x14, 6)
    
    def ntc1_fault(self):
        return self.bf(0x14, 5, 3)
    
    def ntc2_fault(self):
        return self.bf(0x14, 2, 0)
    
    #STATUS4
    def cc1_sink_stat(self):
        return self.bf(0x15, 7, 6)
    
    def cc2_sink_stat(self):
        return self.bf(0x15, 5, 4)
    
    #STATUS5
    def topoff_active(self):
        return self.bf(0x16, 6)
    
    def bfet_stat(self):
        return self.bf(0x16, 5)
    
    def batt_low_stat(self):
        return self.bf(0x16, 4)
    
    def vin_test_high(self):
        return self.bf(0x16, 2)
    
    def debugacc(self):
        return self.bf(0x16, 1)

