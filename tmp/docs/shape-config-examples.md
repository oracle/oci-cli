# OCI Shape Config Examples

## Shape Config Parameters

The shape-config is used when updating compute instances with flexible shapes. Here are the parameters:

- **baselineOcpuUtilization**: Baseline CPU utilization
  - `BASELINE_1_1`: 100% baseline (no burstable performance)
  - `BASELINE_1_2`: 50% baseline (cost-optimized)
  - `BASELINE_1_8`: 12.5% baseline (most cost-effective)
- **memoryInGBs**: Memory in gigabytes (float, minimum 1.0)
- **nvmes**: Number of NVMe drives (integer, optional)
- **ocpus**: Number of OCPUs (float, minimum 1.0)
- **resourceManagement**: Resource management type (string, optional)
- **vcpus**: Number of vCPUs (integer, optional)

## Two Essential Examples

### Example 1: Truly Minimal Configuration
```json
{
  "ocpus": 1.0,
  "memoryInGBs": 1.0
}
```
- **Use case**: Development, testing, minimal workloads
- **Cost**: Absolute minimum
- **Performance**: Basic

### Example 2: Reasonable Small with Baseline Control
```json
{
  "ocpus": 2.0,
  "memoryInGBs": 4.0,
  "baselineOcpuUtilization": "BASELINE_1_1"
}
```
- **Use case**: Small production workloads, consistent performance needed
- **Cost**: Economical
- **Performance**: Predictable with 100% baseline

## Notes

- Minimum memory is 1GB per OCPU
- These examples alternate when using `--generate-param-json-input shape-config`
- Both configurations are production-ready and cost-effective