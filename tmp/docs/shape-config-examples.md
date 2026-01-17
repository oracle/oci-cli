# OCI Shape Config Examples

## Shape Config Parameters

The shape-config is used when updating compute instances with flexible shapes. Here are the parameters:

- **baselineOcpuUtilization**: Baseline CPU utilization (e.g., "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1")
- **memoryInGBs**: Memory in gigabytes (float)
- **nvmes**: Number of NVMe drives (integer)
- **ocpus**: Number of OCPUs (float)
- **resourceManagement**: Resource management type (string)
- **vcpus**: Number of vCPUs (integer)

## Common Examples

### Example 1: Flexible VM with 2 OCPUs and 16GB RAM
```json
{
  "ocpus": 2.0,
  "memoryInGBs": 16.0,
  "baselineOcpuUtilization": "BASELINE_1_1"
}
```

### Example 2: Burstable Instance with 50% baseline
```json
{
  "ocpus": 1.0,
  "memoryInGBs": 8.0,
  "baselineOcpuUtilization": "BASELINE_1_2"
}
```

### Example 3: High Performance with NVMe drives
```json
{
  "ocpus": 4.0,
  "memoryInGBs": 32.0,
  "nvmes": 2,
  "baselineOcpuUtilization": "BASELINE_1_1"
}
```