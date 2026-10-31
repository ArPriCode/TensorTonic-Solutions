def validate_records(records: list, schema: list) -> list:
    results = []
    
    for idx, record in enumerate(records):
        errors = []
        is_valid = True
        
        for col_schema in schema:
            col = col_schema["column"]
            expected_type = col_schema["type"]
            nullable = col_schema["nullable"]
            
            if col not in record:
                errors.append(f"{col}: missing")
                is_valid = False
                continue
                
            val = record[col]
            
            if val is None:
                if not nullable:
                    errors.append(f"{col}: null")
                    is_valid = False
                continue
                
            val_type = type(val)
            type_ok = False
            
            if expected_type == "int":
                if val_type is int and val_type is not bool:
                    type_ok = True
            elif expected_type == "float":
                if (val_type in (int, float)) and val_type is not bool:
                    type_ok = True
            elif expected_type == "str":
                if val_type is str:
                    type_ok = True
                    
            if not type_ok:
                actual_type = val_type.__name__
                errors.append(f"{col}: expected {expected_type}, got {actual_type}")
                is_valid = False
                continue
                
            if expected_type in ("int", "float"):
                min_val = col_schema.get("min")
                max_val = col_schema.get("max")
                
                if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                    errors.append(f"{col}: out of range")
                    is_valid = False
                    
        results.append({
            "record_index": idx,
            "is_valid": is_valid,
            "errors": errors
        })
        
    return results