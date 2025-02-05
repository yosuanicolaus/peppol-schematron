from typing import TypedDict

SCHEMATRON_CEN_PATH = "validation/schematron/CEN-EN16931-UBL.sch"
SCHEMATRON_PEPPOL_PATH = "validation/schematron/PEPPOL-EN16931-UBL.sch"
SCHEMATRON_NLCIUS_PATH = "validation/schematron/SI-UBL-2.0.sch"
SCHEMATRON_EUSR_PATH = "validation/schematron/peppol-end-user-statistics-reporting-1.1.4.sch"
SCHEMATRON_TSR_PATH = "validation/schematron/peppol-transaction-statistics-reporting-1.0.4.sch"
TEST_INVOICE_PATH = "test_files/invoice.xml"
TEST_INVOICE100_PATH = "test_files/invoice100.xml"
TEST_NLCIUS_PATH = "test_files/nlcius.xml"
TEST_EUSR_PATH = "test_files/eusr.xml"
TEST_TSR_PATH = "test_files/tsr.xml"


class TestMapValue(TypedDict):
    schematron_paths: tuple[str, ...]
    test_file_path: str


TEST_MAP: dict[str, TestMapValue] = {
    "peppol": {
        "schematron_paths": (SCHEMATRON_CEN_PATH, SCHEMATRON_PEPPOL_PATH),
        "test_file_path": TEST_INVOICE_PATH,
    },
    "peppol100": {
        "schematron_paths": (SCHEMATRON_CEN_PATH, SCHEMATRON_PEPPOL_PATH),
        "test_file_path": TEST_INVOICE100_PATH,
    },
    "nlcius": {
        "schematron_paths": (SCHEMATRON_CEN_PATH, SCHEMATRON_NLCIUS_PATH),
        "test_file_path": TEST_NLCIUS_PATH,
    },
    "eusr": {
        "schematron_paths": (SCHEMATRON_EUSR_PATH,),
        "test_file_path": TEST_EUSR_PATH,
    },
    "tsr": {
        "schematron_paths": (SCHEMATRON_TSR_PATH,),
        "test_file_path": TEST_TSR_PATH,
    },
    "justpeppol": {
        "schematron_paths": (SCHEMATRON_PEPPOL_PATH,),
        "test_file_path": TEST_INVOICE_PATH,
    },
    "justpeppol100": {
        "schematron_paths": (SCHEMATRON_PEPPOL_PATH,),
        "test_file_path": TEST_INVOICE100_PATH,
    },
    "all": {
        "schematron_paths": (
            SCHEMATRON_CEN_PATH,
            SCHEMATRON_PEPPOL_PATH,
            SCHEMATRON_NLCIUS_PATH,
            SCHEMATRON_EUSR_PATH,
            SCHEMATRON_TSR_PATH,
        ),
        "test_file_path": TEST_INVOICE_PATH,
    },
}


PATH_ROOT_MAP = {
    SCHEMATRON_CEN_PATH: "CEN",
    SCHEMATRON_PEPPOL_PATH: "PEPPOL",
    SCHEMATRON_NLCIUS_PATH: "NLCIUS",
    SCHEMATRON_EUSR_PATH: "EUSR",
    SCHEMATRON_TSR_PATH: "TSR",
}

INVOICE_LINE_TAG = "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoiceLine"

PEPPOL_CONST_ISO3166 = " AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW 1A XI "
PEPPOL_CONST_ISO4217 = " AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BOV BRL BSD BTN BWP BYN BZD CAD CDF CHE CHF CHW CLF CLP CNY COP COU CRC CUC CUP CVE CZK DJF DKK DOP DZD EGP ERN ETB EUR FJD FKP GBP GEL GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LYD MAD MDL MGA MKD MMK MNT MOP MRO MUR MVR MWK MXN MXV MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLL SOS SRD SSP STN SVC SYP SZL THB TJS TMT TND TOP TRY TTD TWD TZS UAH UGX USD USN UYI UYU UZS VEF VND VUV WST XAF XAG XAU XBA XBB XBC XBD XCD XDR XOF XPD XPF XPT XSU XTS XUA XXX YER ZAR ZMW ZWL "
PEPPOL_CONST_MIMECODE = " application/pdf image/png image/jpeg text/csv application/vnd.openxmlformats-officedocument.spreadsheetml.sheet application/vnd.oasis.opendocument.spreadsheet "
PEPPOL_CONST_UNCL2005 = " 3 35 432 "
PEPPOL_CONST_UNCL5189 = " 41 42 60 62 63 64 65 66 67 68 70 71 88 95 100 102 103 104 105 "
PEPPOL_CONST_UNCL7161 = " AA AAA AAC AAD AAE AAF AAH AAI AAS AAT AAV AAY AAZ ABA ABB ABC ABD ABF ABK ABL ABN ABR ABS ABT ABU ACF ACG ACH ACI ACJ ACK ACL ACM ACS ADC ADE ADJ ADK ADL ADM ADN ADO ADP ADQ ADR ADT ADW ADY ADZ AEA AEB AEC AED AEF AEH AEI AEJ AEK AEL AEM AEN AEO AEP AES AET AEU AEV AEW AEX AEY AEZ AJ AU CA CAB CAD CAE CAF CAI CAJ CAK CAL CAM CAN CAO CAP CAQ CAR CAS CAT CAU CAV CAW CAX CAY CAZ CD CG CS CT DAB DAC DAD DAF DAG DAH DAI DAJ DAK DAL DAM DAN DAO DAP DAQ DL EG EP ER FAA FAB FAC FC FH FI GAA HAA HD HH IAA IAB ID IF IR IS KO L1 LA LAA LAB LF MAE MI ML NAA OA PA PAA PC PL RAB RAC RAD RAF RE RF RH RV SA SAA SAD SAE SAI SG SH SM SU TAB TAC TT TV V1 V2 WH XAA YY ZZZ "
PEPPOL_CONST_UNCL5305 = " AE E S Z G O K L M "
PEPPOL_CONST_EAID = " 0002 0007 0009 0037 0060 0088 0096 0097 0106 0130 0135 0142 0151 0183 0184 0188 0190 0191 0192 0193 0195 0196 0198 0199 0200 0201 0202 0204 0208 0209 0210 0211 0212 0213 0215 0216 0218 0221 0230 9901 9910 9913 9914 9915 9918 9919 9920 9922 9923 9924 9925 9926 9927 9928 9929 9930 9931 9932 9933 9934 9935 9936 9937 9938 9939 9940 9941 9942 9943 9944 9945 9946 9947 9948 9949 9950 9951 9952 9953 9957 9959 "


class ForReplaceMapItemValue(TypedDict):
    pattern: str
    replacement: str


# Map of Assert IDs -> Dictionary of pattern and replacement
FOR_REPLACE_MAP: dict[str, ForReplaceMapItemValue] = {
    #######
    # CEN #
    #######
    "BR-53": {
        "pattern": "every $taxcurrency in cbc:TaxCurrencyCode satisfies exists(//cac:TaxTotal/cbc:TaxAmount[@currencyID=$taxcurrency])",
        "replacement": "u:for_every(taxcurrency, cbc:TaxCurrencyCode, exists(//cac:TaxTotal/cbc:TaxAmount[@currencyID=$taxcurrency]))",
    },
    # "BR-CO-15": "every $Currency in cbc:DocumentCurrencyCode satisfies (count(cac:TaxTotal/xs:decimal(cbc:TaxAmount[@currencyID=$Currency])) eq 1) and (cac:LegalMonetaryTotal/xs:decimal(cbc:TaxInclusiveAmount) = round( (cac:LegalMonetaryTotal/xs:decimal(cbc:TaxExclusiveAmount) + cac:TaxTotal/xs:decimal(cbc:TaxAmount[@currencyID=$Currency])) * 10 * 10) div 100)",
    # "BR-S-08": "every $rate in xs:decimal(cbc:Percent) satisfies (((exists(//cac:InvoiceLine[cac:Item/cac:ClassifiedTaxCategory/normalize-space(cbc:ID) = 'S'][cac:Item/cac:ClassifiedTaxCategory/xs:decimal(cbc:Percent) =$rate]) or exists(//cac:AllowanceCharge[cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate])) and ((../xs:decimal(cbc:TaxableAmount - 1) < (sum(../../../cac:InvoiceLine[cac:Item/cac:ClassifiedTaxCategory/normalize-space(cbc:ID)='S'][cac:Item/cac:ClassifiedTaxCategory/xs:decimal(cbc:Percent) =$rate]/xs:decimal(cbc:LineExtensionAmount)) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)))) and (../xs:decimal(cbc:TaxableAmount + 1) > (sum(../../../cac:InvoiceLine[cac:Item/cac:ClassifiedTaxCategory/normalize-space(cbc:ID)='S'][cac:Item/cac:ClassifiedTaxCategory/xs:decimal(cbc:Percent) =$rate]/xs:decimal(cbc:LineExtensionAmount)) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)))))) or (exists(//cac:CreditNoteLine[cac:Item/cac:ClassifiedTaxCategory/normalize-space(cbc:ID) = 'S'][cac:Item/cac:ClassifiedTaxCategory/xs:decimal(cbc:Percent) =$rate]) or exists(//cac:AllowanceCharge[cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate])) and ((../xs:decimal(cbc:TaxableAmount - 1) < (sum(../../../cac:CreditNoteLine[cac:Item/cac:ClassifiedTaxCategory/normalize-space(cbc:ID)='S'][cac:Item/cac:ClassifiedTaxCategory/xs:decimal(cbc:Percent) =$rate]/xs:decimal(cbc:LineExtensionAmount)) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)))) and (../xs:decimal(cbc:TaxableAmount + 1) > (sum(../../../cac:CreditNoteLine[cac:Item/cac:ClassifiedTaxCategory/normalize-space(cbc:ID)='S'][cac:Item/cac:ClassifiedTaxCategory/xs:decimal(cbc:Percent) =$rate]/xs:decimal(cbc:LineExtensionAmount)) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount)) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/normalize-space(cbc:ID)='S'][cac:TaxCategory/xs:decimal(cbc:Percent) = $rate]/xs:decimal(cbc:Amount))))))",
    ##########
    # PEPPOL #
    ##########
    "PEPPOL-EN16931-CL001": {
        "pattern": "",  # Empty pattern means replace everything
        "replacement": f"contains('{PEPPOL_CONST_MIMECODE}', concat(' ', @mimeCode, ' '))",
    },
    "PEPPOL-EN16931-CL007": {
        "pattern": "",
        "replacement": f"contains('{PEPPOL_CONST_ISO4217}', concat(' ', @currencyID, ' '))",
    },
    "PEPPOL-EN16931-P0100": {
        "pattern": r"some \$code in tokenize\('71 80 82 84 102 218 219 331 380 382 383 386 388 393 395 553 575 623 780 817 870 875 876 877', '\\s'\) satisfies normalize-space\(text\(\)\) = \$code",
        "replacement": "contains(' 71 80 82 84 102 218 219 331 380 382 383 386 388 393 395 553 575 623 780 817 870 875 876 877 ', concat(' ', normalize-space(text()), ' '))",
    },
    "PEPPOL-EN16931-CL008": {
        "pattern": "",
        "replacement": f"contains('{PEPPOL_CONST_EAID}', concat(' ', @schemeID, ' '))",
    },
    # "PEPPOL-EN16931-CL001": "some $code in $MIMECODE satisfies @mimeCode = $code",
    # "PEPPOL-EN16931-CL007": "some $code in $ISO4217 satisfies @currencyID = $code",
    # "PEPPOL-EN16931-P0100": "some $code in tokenize('71 80 82 84 102 218 219 331 380 382 383 386 388 393 395 553 575 623 780 817 870 875 876 877', '\\s') satisfies normalize-space(text()) = $code",
    # "PEPPOL-EN16931-CL008": "some $code in $eaid satisfies @schemeID = $code",
    ########
    # EUSR #
    ########
    # "SCH-EUSR-40": "every $st in (eusr:Subset[normalize-space(@type) = 'PerEUC']), $steuc in ($st/eusr:Key[normalize-space(@schemeID) = 'EndUserCountry']) satisfies count(eusr:Subset[normalize-space(@type) ='PerEUC'][every $euc in (eusr:Key[normalize-space(@schemeID) = 'EndUserCountry']) satisfies normalize-space($euc) = normalize-space($steuc)]) = 1",
    # "SCH-EUSR-33": "every $st in (eusr:Subset) satisfies xs:integer($st/eusr:SendingOrReceivingEndUsers) <= xs:integer($st/eusr:SendingEndUsers + $st/eusr:ReceivingEndUsers)",
    # "SCH-EUSR-34": "every $st in (eusr:Subset) satisfies xs:integer($st/eusr:SendingOrReceivingEndUsers) >= xs:integer($st/eusr:SendingEndUsers)",
    # "SCH-EUSR-35": "every $st in (eusr:Subset) satisfies xs:integer($st/eusr:SendingOrReceivingEndUsers) >= xs:integer($st/eusr:ReceivingEndUsers)",
    # "SCH-EUSR-36": "every $st in (eusr:Subset) satisfies xs:integer($st/eusr:SendingOrReceivingEndUsers) > 0",
    #######
    # TSR #
    #######
    # "SCH-TSR-06": "every $key in (tsr:Subtotal[normalize-space(@type) = 'PerTP']/tsr:Key) satisfies count(tsr:Subtotal[normalize-space(@type) = 'PerTP']/tsr:Key[concat(normalize-space(@schemeID),'::',normalize-space(.)) = concat(normalize-space($key/@schemeID),'::',normalize-space($key))]) = 1",
    # "SCH-TSR-28": "every $x in (tsr:Key[normalize-space(@metaSchemeID) = 'SP']) satisfies not(contains(normalize-space($x/@schemeID), ' ')) and contains($cl_spidtype, concat(' ', normalize-space($x/@schemeID), ' '))",
    # "SCH-TSR-34": "every $x in (tsr:Key[normalize-space(@metaSchemeID) = 'SP']) satisfies not(contains(normalize-space($x/@schemeID), ' ')) and contains($cl_spidtype, concat(' ', normalize-space($x/@schemeID), ' '))",
}

TEST_REPLACE_MAP = {
    # CEN
    "BR-CO-10": "number(cbc:LineExtensionAmount) = u:if_else(//cac:InvoiceLine, u:round(sum(//cac:InvoiceLine/cbc:LineExtensionAmount), 2), u:round(sum(//cac:CreditNoteLine/cbc:LineExtensionAmount), 2))",
    "BR-CO-12": "number(cbc:AllowanceTotalAmount) = u:round(sum(../cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cbc:Amount), 2) or (not(cbc:AllowanceTotalAmount) and not(../cac:AllowanceCharge[cbc:ChargeIndicator=false()]))",
    "BR-CO-11": "number(cbc:AllowanceTotalAmount) = (u:round(sum(../cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cbc:Amount), 2)) or (not(cbc:AllowanceTotalAmount) and not(../cac:AllowanceCharge[cbc:ChargeIndicator=false()]))",
    "BR-53": "u:for_every('cbc:TaxCurrencyCode', 'u:exists(//cac:TaxTotal/cbc:TaxAmount[@currencyID=$VAR])')",
    "BR-AE-01": """
        (
            (
                u:exists(//cac:TaxCategory[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:ID[normalize-space() = 'AE']) 
                or 
                u:exists(//cac:ClassifiedTaxCategory[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:ID[normalize-space() = 'AE'])
            )
            and 
            (
                count(
                cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:ID[normalize-space() = 'AE']
                ) = 1
            )
        )
        or 
        (
          not(//cac:TaxCategory[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:ID[normalize-space() = 'AE']) 
          and 
          not(//cac:ClassifiedTaxCategory[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:ID[normalize-space() = 'AE'])
        )
    """,
    "BR-AE-02": """
        (
            u:exists(
                //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'AE'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
            )
            and (
                u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
                or u:exists(
                    //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
                )
            )
            and (
                u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
                or u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID)
            )
        )
        or not(
            u:exists(
                //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'AE'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
            )
        )
    """,
    "BR-AE-03": """
    (
        u:exists(//cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[normalize-space(cbc:ID) = 'AE'][cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]) 
        and 
        (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID) 
            or 
            u:exists(//cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:CompanyID)
        ) 
        and 
        (
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']]/cbc:CompanyID) 
            or 
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID)
        )
    ) 
    or not(
        u:exists(//cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[normalize-space(cbc:ID) = 'AE'][cac:TaxScheme[normalize-space(u:upper_case(cbc:ID)) = 'VAT']])
    )
    """,
    "BR-AE-04": """
    (
        u:exists(//cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'AE'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']])
        and
        (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or
            u:exists(//cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and
        (
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID)
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'AE'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-CO-15": """
        u:for_every('cbc:DocumentCurrencyCode', '(count(cac:TaxTotal/cbc:TaxAmount[@currencyID=$VAR]) = 1) and (number(cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount) = u:round(cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount + cac:TaxTotal/cbc:TaxAmount[@currencyID=$VAR], 2))')
    """,
    "BR-E-01": """
    (
        (
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'E']
            )
            or u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'E']
            )
        )
        and count(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'E']
        ) = 1
    )
    or (
        not(
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'E']
            )
        )
        and not(
            u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'E']
            )
        )
    )
    """,
    "BR-E-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'E'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'E'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-E-03": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='E'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='E'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-E-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='E'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='E'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-G-01": """
    (
        (
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'G']
            )
            or u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'G']
            )
        )
        and count(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'G']
        ) = 1
    )
    or (
        not(
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'G']
            )
        )
        and not(
            u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'G']
            )
        )
    )
    """,
    "BR-G-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'G'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'G'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-G-03": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='G'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='G'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-G-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='G'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='G'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-IC-01": """
    (
        (
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
            )
            or u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
            )
        )
        and count(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
        ) = 1
    )
    or (
        not(
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
            )
        )
        and not(
            u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
            )
        )
    )
    """,
    "BR-IC-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'K'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
        and u:exists(
            //cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'K'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-IC-03": """
    (
        u:exists(
            //cac:allowancecharge[cbc:chargeindicator=false()]/cac:taxcategory[cbc:id[normalize-space(.) = 'k'] and cac:taxscheme/cbc:id[normalize-space(u:upper_case(.))='vat']]
        )
        and (
            u:exists(//cac:accountingsupplierparty/cac:party/cac:partytaxscheme[cac:taxscheme/cbc:id[normalize-space(u:upper_case(.)) = 'vat']]/cbc:companyid)
            or u:exists(
                //cac:taxrepresentativeparty/cac:partytaxscheme[cac:taxscheme/cbc:id[normalize-space(u:upper_case(.)) = 'vat']]/cbc:companyid
            )
        )
        and u:exists(
            //cac:accountingcustomerparty/cac:party/cac:partytaxscheme[cac:taxscheme/cbc:id[normalize-space(u:upper_case(.)) = 'vat']]/cbc:companyid
        )
    )
    or not(
        u:exists(
            //cac:allowancecharge[cbc:chargeindicator=false()]/cac:taxcategory[cbc:id[normalize-space(.) = 'k'] and cac:taxscheme/cbc:id[normalize-space(u:upper_case(.))='vat']]
        )
    )
    """,
    "BR-IC-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'K'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
        and u:exists(
            //cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'K'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-IC-11": """
    (
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
        )
        and (string-length(cac:Delivery/cbc:ActualDeliveryDate) > 1 or boolean(cac:InvoicePeriod/*))
    )
    or not(
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
        )
    )
    """,
    "BR-IC-12": """
    (
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
        )
        and string-length(cac:Delivery/cac:DeliveryLocation/cac:Address/cac:Country/cbc:IdentificationCode) > 1
    )
    or not(
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'K']
        )
    )
    """,
    "BR-IG-01": """
    (
        (
            count(//cac:AllowanceCharge/cac:TaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']])
            +
            count(//cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']])
        ) > 0
        and
        count(cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cbc:ID = 'L']) > 0
    ) or (
        (
            count(//cac:AllowanceCharge/cac:TaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]) + count(//cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']])
        ) = 0 and count(cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
    ) = 0
    )
    """,
    "BR-IG-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-IG-03": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-IG-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='L'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-IP-01": """
    (
        (
            count(//cac:AllowanceCharge/cac:TaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]) + count(//cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']])
        ) > 0 and count(cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cbc:ID = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']) > 0
    ) or (
        (
            count(//cac:AllowanceCharge/cac:TaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]) + count(//cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']])
        ) = 0 and count(cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
    ) = 0
    )
    """,
    "BR-IP-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-IP-03": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-IP-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='M'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-O-01": """
    (
        (
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
            )
            or u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
            )
        )
        and count(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        ) = 1
    )
    or (
        not(
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
            )
        )
        and not(
            u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
            )
        )
    )
    """,
    "BR-O-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and not(
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and not(
            u:exists(//cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and not(
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-O-03": """
    (
        u:exists(
            (/ubl:Invoice|/cn:CreditNote)/cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and not(
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and not(
            u:exists(//cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and not(
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
    )
    or not(
        u:exists(
            (/ubl:Invoice|/cn:CreditNote)/cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-O-04": """
    (
        u:exists(
            (/ubl:Invoice|/cn:CreditNote)/cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and not(
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and not(
            u:exists(//cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
        and not(
            u:exists(//cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID)
        )
    )
    or not(
        u:exists(
            (/ubl:Invoice|/cn:CreditNote)/cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-O-11": """
    (
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
        and count(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cbc:ID[normalize-space(.)!= 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        ) = 0
    )
    or not(
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
    )
    """,
    "BR-O-12": """
    (
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
        and count(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.)!= 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        ) = 0
    )
    or not(
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
    )
    """,
    "BR-O-13": """
    (
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
        and count(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)!= 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        ) = 0
    )
    or not(
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
    )
    """,
    "BR-O-14": """
    (
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
        and count(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)!= 'O'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        ) = 0
    )
    or not(
        u:exists(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'O']
        )
    )
    """,
    "BR-S-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'S'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'S'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-S-03": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='S'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='S'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-S-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='S'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='S'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-Z-01": """
    (
        (
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'Z']
            )
            or u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'Z']
            )
        )
        and count(
            cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'Z']
        ) = 1
    )
    or (
        not(
            u:exists(
                //cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'Z']
            )
        )
        and not(
            u:exists(
                //cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(.)='VAT'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.) = 'Z']
            )
        )
    )
    """,
    "BR-Z-02": """
    (
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'Z'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:ClassifiedTaxCategory[cbc:ID[normalize-space(.) = 'Z'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]
        )
    )
    """,
    "BR-Z-03": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.)='Z'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=false()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'Z'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-Z-04": """
    (
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.)='Z'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
        and (
            u:exists(//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID)
            or u:exists(
                //cac:TaxRepresentativeParty/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.)) = 'VAT']]/cbc:CompanyID
            )
        )
    )
    or not(
        u:exists(
            //cac:AllowanceCharge[cbc:ChargeIndicator=true()]/cac:TaxCategory[cbc:ID[normalize-space(.) = 'Z'] and cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]
        )
    )
    """,
    "BR-CO-04": """
    cac:Item/cac:ClassifiedTaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID
    """,
    "BR-CO-26": """
    u:exists(cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:CompanyID) or u:exists(cac:Party/cac:PartyIdentification/cbc:ID) or u:exists(cac:Party/cac:PartyLegalEntity/cbc:CompanyID)
    """,
    "BR-CO-14": """
    (number(cbc:TaxAmount) = u:round(sum(cac:TaxSubtotal/cbc:TaxAmount), 2)) or not(boolean(cac:TaxSubtotal))
    """,
    "BR-47": """
    u:exists(cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID)
    """,
    "BR-48": """
    u:exists(cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:Percent) or (cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:ID[normalize-space(.)='O'])
    """,
    "BR-CO-17": """
    (
        round(cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:Percent) = 0 and round(cbc:TaxAmount) = 0
    ) or (
        round(cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:Percent)!= 0 and (
            u:abs(cbc:TaxAmount) - 1 < u:round(u:abs(cbc:TaxableAmount) * (cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:Percent div 100), 2) and u:abs(cbc:TaxAmount) + 1 > u:round(u:abs(cbc:TaxableAmount) * (cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:Percent div 100), 2)
        )
    ) or (
        not(
            u:exists(
                cac:TaxCategory[cac:TaxScheme/cbc:ID[normalize-space(u:upper_case(.))='VAT']]/cbc:Percent
            )
        ) and round(cbc:TaxAmount) = 0
    )
    """,
    "BR-S-08": """
    u:for_every(
        'cbc:Percent',
        \"u:if_else(
            u:exists(//cac:InvoiceLine[cac:Item/cac:ClassifiedTaxCategory/cbc:ID[normalize-space(.) = 'S'] and cac:Item/cac:ClassifiedTaxCategory/cbc:Percent = $VAR]/cbc:LineExtensionAmount) or u:exists(//cac:AllowanceCharge[cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount),
            (
              ../cbc:TaxableAmount - 1 < (
                    sum(../../../cac:InvoiceLine[cac:Item/cac:ClassifiedTaxCategory/cbc:ID[normalize-space(.)='S'] and cac:Item/cac:ClassifiedTaxCategory/cbc:Percent = $VAR]/cbc:LineExtensionAmount) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount)
                )
                and../cbc:TaxableAmount + 1 > (
                    sum(../../../cac:InvoiceLine[cac:Item/cac:ClassifiedTaxCategory/cbc:ID[normalize-space(.)='S'] and cac:Item/cac:ClassifiedTaxCategory/cbc:Percent = $VAR]/cbc:LineExtensionAmount) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount)
                )
            ),
            u:if_else(
                u:exists(//cac:CreditNoteLine[cac:Item/cac:ClassifiedTaxCategory/cbc:ID[normalize-space(.) = 'S'] and cac:Item/cac:ClassifiedTaxCategory/cbc:Percent = $VAR]/cbc:LineExtensionAmount) or u:exists(//cac:AllowanceCharge[cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount),
                (
                  ../cbc:TaxableAmount - 1 < (
                        sum(../../../cac:CreditNoteLine[cac:Item/cac:ClassifiedTaxCategory/cbc:ID[normalize-space(.)='S'] and cac:Item/cac:ClassifiedTaxCategory/cbc:Percent = $VAR]/cbc:LineExtensionAmount) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount)
                    )
                    and../cbc:TaxableAmount + 1 > (
                        sum(../../../cac:CreditNoteLine[cac:Item/cac:ClassifiedTaxCategory/cbc:ID[normalize-space(.)='S'] and cac:Item/cac:ClassifiedTaxCategory/cbc:Percent = $VAR]/cbc:LineExtensionAmount) + sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=true()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount) - sum(../../../cac:AllowanceCharge[cbc:ChargeIndicator=false()][cac:TaxCategory/cbc:ID[normalize-space(.)='S'] and cac:TaxCategory/cbc:Percent = $VAR]/cbc:Amount)
                    )
                ),
                true()
            )
        )\"
    )
    """,
    "BR-S-09": """
    (
        u:abs(../cbc:TaxAmount) - 1 < u:round((u:abs(../cbc:TaxableAmount) * (cbc:Percent div 100)), 2)
    ) and (
        u:abs(../cbc:TaxAmount) + 1 > u:round((u:abs(../cbc:TaxableAmount) * (cbc:Percent div 100)), 2)
    )
    """,
    "UBL-SR-12": """
        count(cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[u:upper_case(.)='VAT']]/cbc:CompanyID) <= 1
    """,
    "UBL-SR-13": """
        count(cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[u:upper_case(.)!='VAT']]/cbc:CompanyID) <= 1
    """,
    "UBL-SR-18": """
        count(cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme[cac:TaxScheme/cbc:ID[u:upper_case(.)='VAT']]/cbc:CompanyID) <= 1
    """,
    # PEPPOL
    "PEPPOL-EN16931-R054": "count(cac:TaxTotal[not(cac:TaxSubtotal)]) = u:if_else(//cbc:TaxCurrencyCode, 1, 0)",
    "PEPPOL-EN16931-CL001": f"contains('{PEPPOL_CONST_MIMECODE}', concat(' ', @mimeCode, ' '))",
    "PEPPOL-EN16931-CL007": f"contains('{PEPPOL_CONST_ISO4217}', concat(' ', @currencyID, ' '))",
    "PEPPOL-EN16931-P0100": "$profile != '01' or contains(' 71 80 82 84 102 218 219 331 380 382 383 386 388 393 395 553 575 623 780 817 870 875 876 877 ', concat(' ', normalize-space(text()), ' '))",
    "PEPPOL-EN16931-CL008": f"contains('{PEPPOL_CONST_EAID}', concat(' ', @schemeID, ' '))",
    "PEPPOL-EN16931-F001": "string-length(text()) = 10 and u:call_elementpath(\"'%s' castable as xs:date\", string(.))",
}
