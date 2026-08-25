<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessEvaluationsApi* | [**get_access_evaluation_log**](docs/AccessEvaluationsApi.md#get_access_evaluation_log) | **GET** /api/access/{id} | [EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation. This endpoint will be deprecated in the near future.
*AccessEvaluationsApi* | [**list_access_evaluation_logs**](docs/AccessEvaluationsApi.md#list_access_evaluation_logs) | **GET** /api/access | [EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control
*AuditingApi* | [**create_entry**](docs/AuditingApi.md#create_entry) | **POST** /api/auditing/entries | [EARLY ACCESS] CreateEntry: Create (persist) and audit entry..
*AuditingApi* | [**get_processes**](docs/AuditingApi.md#get_processes) | **GET** /api/auditing/processes | [EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.
*AuditingApi* | [**list_entries**](docs/AuditingApi.md#list_entries) | **GET** /api/auditing/entries | [EARLY ACCESS] ListEntries: Get the audit entries.
*CandelaTracesApi* | [**get_trace_diagram**](docs/CandelaTracesApi.md#get_trace_diagram) | **GET** /api/candelatraces/{traceId}/diagram | [EARLY ACCESS] GetTraceDiagram: Get the diagram representation for a specific trace.
*CandelaTracesApi* | [**get_trace_log**](docs/CandelaTracesApi.md#get_trace_log) | **GET** /api/candelatraces/{traceId} | [EARLY ACCESS] GetTraceLog: Get the log for a specific trace.
*CandelaTracesApi* | [**list_trace_event_logs**](docs/CandelaTracesApi.md#list_trace_event_logs) | **GET** /api/candelatraces/{traceId}/events | [EARLY ACCESS] ListTraceEventLogs: Get the trace event logs for a specific trace.
*CandelaTracesApi* | [**list_trace_logs**](docs/CandelaTracesApi.md#list_trace_logs) | **GET** /api/candelatraces | [EARLY ACCESS] ListTraceLogs: Get the logs for traces.
*LogMetadataApi* | [**list_queryable_fields**](docs/LogMetadataApi.md#list_queryable_fields) | **GET** /api/metadata/logs | [EARLY ACCESS] ListQueryableFields: List the queryable fields for every supported log type.
*MetricsApi* | [**get_metrics**](docs/MetricsApi.md#get_metrics) | **GET** /api/metrics | [EARLY ACCESS] GetMetrics: Get the aggregated platform metrics for the caller's domain.
*RequestsApi* | [**get_request**](docs/RequestsApi.md#get_request) | **GET** /api/requests/{id}/request | GetRequest: Get the request content for a specific API request.
*RequestsApi* | [**get_request_log**](docs/RequestsApi.md#get_request_log) | **GET** /api/requests/{id} | GetRequestLog: Get the log for a specific API request.
*RequestsApi* | [**get_response**](docs/RequestsApi.md#get_response) | **GET** /api/requests/{id}/response | GetResponse: Get the response for a specific API request.
*RequestsApi* | [**list_request_logs**](docs/RequestsApi.md#list_request_logs) | **GET** /api/requests | ListRequestLogs: Get the logs for API requests.
*RequestsApi* | [**query_request_logs**](docs/RequestsApi.md#query_request_logs) | **POST** /api/requests/$query | QueryRequestLogs: Query the logs for API requests, returning only the caller-specified fields in addition to the always-required fields (Timestamp, Id, Application, Operation). The server fetches only the requested columns from the underlying data source to minimise payload and query time.
*VendorLogsApi* | [**get_vendor_log**](docs/VendorLogsApi.md#get_vendor_log) | **GET** /api/vendor/{id} | [EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.
*VendorLogsApi* | [**get_vendor_request**](docs/VendorLogsApi.md#get_vendor_request) | **GET** /api/vendor/{id}/request | [EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.
*VendorLogsApi* | [**get_vendor_response**](docs/VendorLogsApi.md#get_vendor_response) | **GET** /api/vendor/{id}/response | [EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.
*VendorLogsApi* | [**list_vendor_logs**](docs/VendorLogsApi.md#list_vendor_logs) | **GET** /api/vendor | [EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.


<a id="documentation-for-models"></a>
## Documentation for Models

 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [AccessEvaluationLog](docs/AccessEvaluationLog.md)
 - [ActionId](docs/ActionId.md)
 - [AuditData](docs/AuditData.md)
 - [AuditDataSummary](docs/AuditDataSummary.md)
 - [AuditEntry](docs/AuditEntry.md)
 - [AuditEntryNote](docs/AuditEntryNote.md)
 - [AuditProcess](docs/AuditProcess.md)
 - [AuditProcessSummary](docs/AuditProcessSummary.md)
 - [BooleanComparator](docs/BooleanComparator.md)
 - [Bucket](docs/Bucket.md)
 - [CreateAuditEntry](docs/CreateAuditEntry.md)
 - [DateComparator](docs/DateComparator.md)
 - [Histogram](docs/Histogram.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [IdentifierPartSchema](docs/IdentifierPartSchema.md)
 - [IdentityMetricsDataSet](docs/IdentityMetricsDataSet.md)
 - [InsightsFilter](docs/InsightsFilter.md)
 - [Link](docs/Link.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [MetricDataSetFailure](docs/MetricDataSetFailure.md)
 - [MetricsResponse](docs/MetricsResponse.md)
 - [NumericComparator](docs/NumericComparator.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [QueriedRequestLog](docs/QueriedRequestLog.md)
 - [QueryRequestLogsRequest](docs/QueryRequestLogsRequest.md)
 - [QueryableLogField](docs/QueryableLogField.md)
 - [QueryableLogType](docs/QueryableLogType.md)
 - [RelativeBoundary](docs/RelativeBoundary.md)
 - [RelativeOffset](docs/RelativeOffset.md)
 - [Request](docs/Request.md)
 - [RequestLog](docs/RequestLog.md)
 - [RequestsPerMinuteBucket](docs/RequestsPerMinuteBucket.md)
 - [RequestsPerMinuteDataSet](docs/RequestsPerMinuteDataSet.md)
 - [Resource](docs/Resource.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [ResourceListOfAuditProcessSummary](docs/ResourceListOfAuditProcessSummary.md)
 - [ResourceListOfQueriedRequestLog](docs/ResourceListOfQueriedRequestLog.md)
 - [ResourceListOfQueryableLogType](docs/ResourceListOfQueryableLogType.md)
 - [ResourceListOfTraceEventLog](docs/ResourceListOfTraceEventLog.md)
 - [ResourceListOfTraceLog](docs/ResourceListOfTraceLog.md)
 - [ResourceListWithHistogramOfAccessEvaluationLog](docs/ResourceListWithHistogramOfAccessEvaluationLog.md)
 - [ResourceListWithHistogramOfRequestLog](docs/ResourceListWithHistogramOfRequestLog.md)
 - [ResourceListWithHistogramOfVendorLog](docs/ResourceListWithHistogramOfVendorLog.md)
 - [Response](docs/Response.md)
 - [ScrollableCollectionOfAuditEntry](docs/ScrollableCollectionOfAuditEntry.md)
 - [ServiceEndpointDuration](docs/ServiceEndpointDuration.md)
 - [ServiceEndpointDurations24hDataSet](docs/ServiceEndpointDurations24hDataSet.md)
 - [ServiceRequests](docs/ServiceRequests.md)
 - [ServiceRequests24hDataSet](docs/ServiceRequests24hDataSet.md)
 - [TextComparator](docs/TextComparator.md)
 - [TimeRange](docs/TimeRange.md)
 - [TraceDiagramEdge](docs/TraceDiagramEdge.md)
 - [TraceDiagramNode](docs/TraceDiagramNode.md)
 - [TraceDiagramResponse](docs/TraceDiagramResponse.md)
 - [TraceEventLog](docs/TraceEventLog.md)
 - [TraceLog](docs/TraceLog.md)
 - [VendorLog](docs/VendorLog.md)
 - [VendorRequest](docs/VendorRequest.md)
 - [VendorResponse](docs/VendorResponse.md)

