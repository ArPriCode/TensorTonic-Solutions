from collections import defaultdict
import bisect

def point_in_time_join(events: list, feature_rows: list, ttl: int) -> list:
    grouped_rows = defaultdict(list)
    for row in feature_rows:
        grouped_rows[row["entity_id"]].append((row["timestamp"], row["value"]))
    
    grouped_timestamps = {}
    grouped_values = {}
    for entity_id, rows in grouped_rows.items():
        rows.sort(key=lambda x: x[0])
        grouped_timestamps[entity_id] = [r[0] for r in rows]
        grouped_values[entity_id] = [r[1] for r in rows]
        
    result = []
    for event in events:
        entity_id = event["entity_id"]
        e_time = event["timestamp"]
        
        val = None
        if entity_id in grouped_timestamps:
            ts_list = grouped_timestamps[entity_id]
            idx = bisect.bisect_right(ts_list, e_time) - 1
            if idx >= 0:
                match_ts = ts_list[idx]
                if e_time - match_ts <= ttl:
                    val = grouped_values[entity_id][idx]
                    
        result.append({
            "entity_id": entity_id,
            "timestamp": e_time,
            "value": val
        })
        
    return result