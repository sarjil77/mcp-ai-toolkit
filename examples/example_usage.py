#!/usr/bin/env python3
"""
Example usage of the insurance MCP Server
This demonstrates how to use the server to process insurance certificate PDFs
"""

import json
import sys
import os

# Add the parent directory to the path so we can import from servers
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from servers.insurance_server import (
    process_insurance_certificate,
    get_certificate_holder_info,
    get_coverage_details,
    get_insured_information,
    get_producer_information,
    validate_certificate_signature
)

def main():
    # Example PDF file path - replace with your actual PDF file
    pdf_file_path = "/path/to/your/insurance_certificate.pdf"
    
    print("=== insurance MCP Server Example ===\n")
    
    # 1. Process the full certificate
    print("1. Processing full insurance certificate...")
    full_result = process_insurance_certificate(pdf_file_path)
    print(f"Success: {full_result.get('Success', 'Unknown')}")
    print(f"Request ID: {full_result.get('RequestId', 'N/A')}")
    print(f"Classification: {full_result.get('Classification', 'N/A')}")
    print()
    
    # 2. Get certificate holder information
    print("2. Certificate Holder Information:")
    holder_info = get_certificate_holder_info(pdf_file_path)
    print(f"Name: {holder_info.get('Name', 'N/A')}")
    print(f"Address: {holder_info.get('Address', 'N/A')}")
    print(f"City: {holder_info.get('City', 'N/A')}, {holder_info.get('StateName', 'N/A')} {holder_info.get('ZipCode', 'N/A')}")
    print()
    
    # 3. Get insured information
    print("3. Insured Information:")
    insured_info = get_insured_information(pdf_file_path)
    print(f"Name: {insured_info.get('Name', 'N/A')}")
    print(f"Address: {insured_info.get('Address', 'N/A')}")
    print(f"City: {insured_info.get('City', 'N/A')}, {insured_info.get('StateName', 'N/A')} {insured_info.get('ZipCode', 'N/A')}")
    print(f"Phone: {insured_info.get('Phone', 'N/A')}")
    print()
    
    # 4. Get producer information
    print("4. Producer Information:")
    producer_info = get_producer_information(pdf_file_path)
    print(f"Name: {producer_info.get('Name', 'N/A')}")
    print(f"Address: {producer_info.get('Address', 'N/A')}")
    print(f"Phone: {producer_info.get('Phone', 'N/A')}")
    print(f"Email: {producer_info.get('Email', 'N/A')}")
    print()
    
    # 5. Check certificate signature
    print("5. Certificate Signature Status:")
    signature_info = validate_certificate_signature(pdf_file_path)
    print(f"Signed: {signature_info.get('signed', 'N/A')}")
    print(f"Files: {signature_info.get('filename', [])}")
    print()
    
    # 6. Get coverage details
    print("6. Coverage Details:")
    coverages = get_coverage_details(pdf_file_path)
    for i, coverage in enumerate(coverages):
        print(f"Coverage {i+1} (ID: {coverage.get('CoverageId', 'N/A')}):")
        
        # Policy info
        policy_info = coverage.get('PolicyInfo', [{}])[0]
        print(f"  Carrier: {policy_info.get('CarrierName', 'N/A')}")
        print(f"  Policy Number: {policy_info.get('PolicyNumber', 'N/A')}")
        print(f"  Policy Period: {policy_info.get('PolicyStartDate', 'N/A')} - {policy_info.get('PolicyEndDate', 'N/A')}")
        
        # Limits
        limits = coverage.get('Limits', [])
        if limits:
            print(f"  Limits:")
            for limit in limits:
                print(f"    {limit.get('Title', 'N/A')}: {limit.get('Price', 'N/A')}")
        
        print()

if __name__ == "__main__":
    main()
