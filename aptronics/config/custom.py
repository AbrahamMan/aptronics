from __future__ import unicode_literals
import pdb
import frappe,json
from frappe import _, msgprint, throw


def get_custom_series(doc, method=None):
    try:
        name = frappe.get_value(doc.doctype,doc.name,'name')
        if name == None:
            #frappe.msgprint("Insert")
            doc.name = get_series(doc, doc.customer_name[:3])
            #frappe.msgprint(series)
            return doc
        else:
            pass
    except:
        frappe.msgprint(_("Something broke"))
        doc.name = get_series(doc, doc.customer_name[:3])
        return doc

def get_series(doc, prefix):
    if doc.doctype == 'Customer':
        #try:
        if doc.customer_type == 'Company':
            name = frappe.get_value('Customer',{'customer_name':doc.customer_name,
                                                'customer_type': 'Company'}
                                               ,'name')
            if name:
                customer = frappe.get_doc('Customer', name)
            else:
                return check_series(doc,prefix)

            if doc.tax_id == None:
                doctax_id = 'Unknown'
            else:
                doctax_id = doc.tax_id

            if customer.tax_id == None:
                customertax_id = 'Unknown'
            else:
                customertax_id = customer.tax_id

            if customertax_id != 'Unknown':
                if doctax_id != 'Unknown':
                    if customertax_id == doctax_id:
                        return customer.name
                    else:
                        return check_series(doc,prefix)
                else:
                    return customer.name
            else:
                return customer.name

        else:
            #try:
            customer = frappe.get_doc({
                "doctype":'Customer',
                'customer_name':doc.customer_name,
                'customer_type':'Individual'
            })
                #frappe.db.sql("select count(`name`) as n, tax_id from `tabCustomer` where customer_name = '" + doc.customer_name + "'", as_dict=1)[0]
            frappe.msgprint(customer.name)

            if doc.tax_id != None:
                if customer.tax_id != '' and customer.tax_i == doc.tax_id:
                    prefix = customer.name
                elif customer.tax_id == '':
                    prefix = customer.name
            else:
                if customer.tax_id == '':
                    prefix = customer.name

#                    if doc.tax_id != None:
#                       customerNameCount = frappe.db.sql("select count(`name`) as n from `tabCustomer` where tax_id = '" + doc.tax_id + "'")[0][0]
#                      #frappe.msgprint(customerNameCount)
#                     if customerNameCount >0:
#                        frappe.throw(_("Duplicate company name with tax_id = " + doc.tax_id))
            #except Exception as e:
            #    frappe.msgprint(_(e.message))

        #except Exception as e:
         #   frappe.msgprint(_(e.message))

    elif doc.doctype == 'Supplier':
        prefix = doc.supplier_name[:3]
        try:
            try:
                supplier = frappe.get_doc("Supplier",{'supplier_name':doc.supplier_name}, 'name')
                    #frappe.db.sql("select count(`name`) as n from `tabCustomer` where customer_name = '" + doc.customer_name + "'")[0][0]
                #frappe.msgprint(customerNameCount)
                if supplier:
                    prefix = supplier
            except Exception as e:
                frappe.msgprint(_(e.message))
        except Exception as e:
            frappe.msgprint(_(e.message))
    elif doc.doctype == 'Contact':
        prefix = doc.first_name[:3]
        try:
            contact = frappe.get_doc("Contact",{'first_name':doc.first_name, 'last_name':doc.last_name, 'email_id':doc.email_id}, 'name')
                #frappe.db.sql("select count(`name`) as n from `tabCustomer` where customer_name = '" + doc.customer_name + "'")[0][0]
            #frappe.msgprint(customerNameCount)
            if contact:
                prefix = contact
        except Exception as e:
            frappe.msgprint(_(e.message))


def check_series(doc, prefix):
    frappe.msgprint(prefix)
    countCustomer = frappe.db.sql("select count(`name`) as n from `tabCustomer` where customer_name like '" + prefix.upper() + "%'")[0][0]
    countSupplier = frappe.db.sql("select count(`name`) as n from `tabSupplier` where supplier_name like '" + prefix.upper() + "%'")[0][0]
    countContact = frappe.db.sql("select count(`name`) as n from `tabContact` where first_name like '" + prefix.upper() + "%'")[0][0]

    count = countCustomer + countContact + countSupplier + 1
    frappe.msgprint(count)
    series = prefix.upper() + '{:03d}'.format(count)

    while 1:
        countCustomer = frappe.db.sql("select count(`name`) as n from `tabCustomer` where name = '" + series + "'")[0][0]
        countSupplier = frappe.db.sql("select count(`name`) as n from `tabSupplier` where name = '" + series + "'")[0][0]
        countContact = frappe.db.sql("select count(`name`) as n from `tabContact` where name = '" + series + "'")[0][0]

        if (countCustomer + countSupplier + countContact) != 0:
            count = count + 1
            #frappe.msgprint(count)
            series = prefix.upper() + '{:03d}'.format(count)
        else:
            break

    frappe.msgprint(_(series))
    return series
