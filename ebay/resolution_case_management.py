import urllib2
from lxml import etree

from ConfigParser import ConfigParser
from utils import relative

# case retrieval calls
def getUserCases(caseStatusFilter=None, caseTypeFilter=None, creationDateRangeFilterFrom=None, creationDateRangeFilterTo=None, itemFilter=None, paginationInput=None, sortOrder=None):
    root = etree.Element("getUserCasesRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    #caseStatusFilter is a List
    if caseStatusFilter:
        caseStatusFilter_elem = etree.SubElement(root, "caseStatusFilter")
        for status in caseStatusFilter:
            caseStatus_elem = etree.SubElement(caseStatusFilter_elem, "caseStatus")
            caseStatus_elem.text = status

    #caseTypeFilter is a List
    if caseTypeFilter:
        caseTypeFilter_elem = etree.SubElement(root, "caseTypeFilter")
        for case_type in caseTypeFilter:
            caseType_elem = etree.SubElement(caseStatusFilter_elem, "caseType")
            caseType_elem.text = case_type

    if creationDateRangeFilterFrom and creationDateRangeFilterTo:
        creationDateRangeFilter_elem = etree.SubElement(root, "creationDateRangeFilter")

        creationDateRangeFilterFrom_elem = etree.SubElement(creationDateRangeFilter_elem, "fromDate")
        creationDateRangeFilterFrom_elem.text = creationDateRangeFilterFrom 
        creationDateRangeFilterTo_elem = etree.SubElement(creationDateRangeFilter_elem, "toDate")
        creationDateRangeFilterTo_elem.text = creationDateRangeFilterTo


    #itemFilter is a dict: {itemId:123, transactionId:72}
    if itemFilter and len(itemFilter)>0:
        itemFilter_elem = etree.SubElement(root, "itemFilter")
        for key in itemFilter.keys(): 
            itemId_elem = etree.SubElement(itemFilter_elem, key)
            itemId_elem.text =  itemFilter[key]


    # paginationInput is a dict: {entriesPerPage:5, pageNumber:10}    
    if paginationInput and len(paginationInput)>0:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput.keys():
            input_values_elem = etree.SubElement(paginationInput_elem, keys)
            input_values_elem.text = paginationInput[key]

    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder
        
        
    request = etree.tostring(root, pretty_print=True)
    return get_response(getUserCases.__name__, request)
    
def getEBPCaseDetail(caseId, caseType):
    root = etree.Element("getEBPCaseDetailRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(getEBPCaseDetail.__name__, request)
    

# Seller Option Calls
def provideTrackingInfo(caseId, caseType, carrierUsed, trackingNumber, comments=None):
    root = etree.Element("provideTrackingInfoRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
   
    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType

    carrierUsed_elem = etree.SubElement(root, "carrierUsed")
    carrierUsed_elem.text = carrierUsed
    
    trackingNumber_elem = etree.SubElement(root, "trackingNumber")
    trackingNumber_elem.text = trackingNumber

    if comments:
        comments_elem = etree.SubElement(root, "comments")
        comments_elem.text = comments
        
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(provideTrackingInfo.__name__, request)
    
def issueFullRefund(caseId, caseType, comments=None):
    root = etree.Element("issueFullRefundRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    
    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType
    
    if comments:
        comments_elem = etree.SubElement(root, "comments")
        comments_elem.text = comments
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(issueFullRefund.__name__, request)
    
def offerOtherSolution(caseId, caseType, messageToBuyer):
    root = etree.Element("offerOtherSolutionRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType
    
    messageToBuyer_elem = etree.SubElement(root, "messageToBuyer")
    messageToBuyer_elem.text = messageToBuyer
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(offerOtherSolution.__name__, request)
    
def escalateToCustomerSuppport(caseId, caseType, escalationReason, comments=None):
    root = etree.Element("escalateToCustomerSuppportRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType
    
    #escalationReason is a dict
    escalationReason_elem = etree.SubElement(root, "escalationReason")
    for key in escalationReason.keys():
        key_elem = etree.SubElement(root, key)
        key_elem.text = escalationReason[key]
    
    if comments:
        comments_elem = etree.SubElement(root, "comments")
        comments_elem.text = comments
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(escalateToCustomerSuppport.__name__, request)
    
def appealToCustomerSupport(caseId, caseType, appealReason, comments=None):
    root = etree.Element("appealToCustomerSupportRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    
    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType

    appealReason_elem = etree.SubElement(root, "appealReason")
    appealReason_elem.text = appealReason 
    
    if comments:
        comments_elem = etree.SubElement(root, "comments")
        comments_elem.text = comments
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(appealToCustomerSupport.__name__, request)
    

# Metadata calls
def getActivityOptions(caseId, caseType):
    root = etree.Element("getActivityOptionsRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    caseId_elem = etree.SubElement(root, "caseId")
    id_elem = etree.SubElement(caseId_elem, "id")
    id_elem.text = caseId
    type_elem = etree.SubElement(caseId_elem, "type")
    type_elem.text = caseType
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(getActivityOptions.__name__, request)
    
def getVersion():
    root = etree.Element("getVersionRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(getVersion.__name__, request)


def get_response(operation_name, data):
    endpoint='https://svcs.sandbox.ebay.com/services/resolution/ResolutionCaseManagementService/v1'
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    access_token = config.get("auth", "token")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-TOKEN": access_token}
    
    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data
