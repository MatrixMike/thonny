# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: exa/language_server_pb/language_server.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'exa/language_server_pb/language_server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from exa.chat_pb import chat_pb2 as exa_dot_chat__pb_dot_chat__pb2
from exa.codeium_common_pb import codeium_common_pb2 as exa_dot_codeium__common__pb_dot_codeium__common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,exa/language_server_pb/language_server.proto\x12\x16\x65xa.language_server_pb\x1a\x16\x65xa/chat_pb/chat.proto\x1a*exa/codeium_common_pb/codeium_common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x02\n\x15GetCompletionsRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12<\n\x08\x64ocument\x18\x02 \x01(\x0b\x32 .exa.language_server_pb.DocumentR\x08\x64ocument\x12K\n\x0e\x65\x64itor_options\x18\x03 \x01(\x0b\x32$.exa.codeium_common_pb.EditorOptionsR\reditorOptions\x12I\n\x0fother_documents\x18\x05 \x03(\x0b\x32 .exa.language_server_pb.DocumentR\x0eotherDocuments\x12\x1d\n\nmodel_name\x18\n \x01(\tR\tmodelName\"\xa0\x01\n\x16GetCompletionsResponse\x12\x33\n\x05state\x18\x01 \x01(\x0b\x32\x1d.exa.language_server_pb.StateR\x05state\x12Q\n\x10\x63ompletion_items\x18\x02 \x03(\x0b\x32&.exa.language_server_pb.CompletionItemR\x0f\x63ompletionItems\"{\n\x17\x41\x63\x63\x65ptCompletionRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12#\n\rcompletion_id\x18\x02 \x01(\tR\x0c\x63ompletionId\"\x1a\n\x18\x41\x63\x63\x65ptCompletionResponse\"O\n\x10HeartbeatRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\"\x13\n\x11HeartbeatResponse\"\x15\n\x13GetAuthTokenRequest\"I\n\x14GetAuthTokenResponse\x12\x1d\n\nauth_token\x18\x01 \x01(\tR\tauthToken\x12\x12\n\x04uuid\x18\x02 \x01(\tR\x04uuid\"\x85\x01\n\x12RecordEventRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12\x32\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x1c.exa.codeium_common_pb.EventR\x05\x65vent\"\x15\n\x13RecordEventResponse\"r\n\x14\x43\x61ncelRequestRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12\x1d\n\nrequest_id\x18\x02 \x01(\x04R\trequestId\"\x17\n\x15\x43\x61ncelRequestResponse\"\r\n\x0b\x45xitRequest\"\x0e\n\x0c\x45xitResponse\"\x15\n\x13GetProcessesRequest\"\x8c\x01\n\x14GetProcessesResponse\x12\x19\n\x08lsp_port\x18\x01 \x01(\rR\x07lspPort\x12/\n\x14\x63hat_web_server_port\x18\x02 \x01(\rR\x11\x63hatWebServerPort\x12(\n\x10\x63hat_client_port\x18\x03 \x01(\rR\x0e\x63hatClientPort\"\x89\x04\n\x15GetChatMessageRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12\x16\n\x06prompt\x18\x02 \x01(\tR\x06prompt\x12=\n\rchat_messages\x18\x03 \x03(\x0b\x32\x18.exa.chat_pb.ChatMessageR\x0c\x63hatMessages\x12U\n\x11\x65xperiment_config\x18\x04 \x01(\x0b\x32(.exa.language_server_pb.ExperimentConfigR\x10\x65xperimentConfig\x12I\n\x0f\x61\x63tive_document\x18\x05 \x01(\x0b\x32 .exa.language_server_pb.DocumentR\x0e\x61\x63tiveDocument\x12.\n\x13open_document_paths\x18\x06 \x03(\tR\x11openDocumentPaths\x12\'\n\x0fworkspace_paths\x18\x07 \x03(\tR\x0eworkspacePaths\x12\x61\n\x16\x63ontext_inclusion_type\x18\x08 \x01(\x0e\x32+.exa.codeium_common_pb.ContextInclusionTypeR\x14\x63ontextInclusionType\"U\n\x16GetChatMessageResponse\x12;\n\x0c\x63hat_message\x18\x01 \x01(\x0b\x32\x18.exa.chat_pb.ChatMessageR\x0b\x63hatMessage\"\x84\x02\n\x19RecordChatFeedbackRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12\x1d\n\nmessage_id\x18\x02 \x01(\tR\tmessageId\x12\x39\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x03 \x01(\x0e\x32\x1d.exa.chat_pb.ChatFeedbackTypeR\x08\x66\x65\x65\x64\x62\x61\x63k\x12\x16\n\x06reason\x18\x04 \x01(\tR\x06reason\x12\x38\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\x1c\n\x1aRecordChatFeedbackResponse\"\xe2\x01\n\x1dRecordChatPanelSessionRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12\x43\n\x0fstart_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0estartTimestamp\x12?\n\rend_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x65ndTimestamp\" \n\x1eRecordChatPanelSessionResponse\"\xaf\x01\n\x16\x43lusteredSearchRequest\x12;\n\x08metadata\x18\x04 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\x1f\n\x0bnum_results\x18\x02 \x01(\rR\nnumResults\x12!\n\x0cnum_clusters\x18\x03 \x01(\rR\x0bnumClusters\"\x7f\n\x17\x43lusteredSearchResponse\x12G\n\x08\x63lusters\x18\x01 \x03(\x0b\x32+.exa.language_server_pb.SearchResultClusterR\x08\x63lusters\x12\x1b\n\tsearch_id\x18\x02 \x01(\tR\x08searchId\"\xd7\x01\n\x12\x45xactSearchRequest\x12;\n\x08metadata\x18\x03 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\x12>\n\x05query\x18\x01 \x01(\x0b\x32(.exa.language_server_pb.ExactSearchQueryR\x05query\x12\x44\n\x07options\x18\x02 \x01(\x0b\x32*.exa.language_server_pb.ExactSearchOptionsR\x07options\"\x94\x01\n\x13\x45xactSearchResponse\x12\x43\n\x07results\x18\x01 \x03(\x0b\x32).exa.language_server_pb.ExactSearchResultR\x07results\x12\x1b\n\thit_limit\x18\x02 \x01(\x08R\x08hitLimit\x12\x1b\n\tsearch_id\x18\x03 \x01(\tR\x08searchId\":\n\x1a\x41\x64\x64TrackedWorkspaceRequest\x12\x1c\n\tworkspace\x18\x01 \x01(\tR\tworkspace\"\x1d\n\x1b\x41\x64\x64TrackedWorkspaceResponse\"=\n\x1dRemoveTrackedWorkspaceRequest\x12\x1c\n\tworkspace\x18\x01 \x01(\tR\tworkspace\" \n\x1eRemoveTrackedWorkspaceResponse\"\xeb\x01\n!RefreshContextForIdeActionRequest\x12I\n\x0f\x61\x63tive_document\x18\x01 \x01(\x0b\x32 .exa.language_server_pb.DocumentR\x0e\x61\x63tiveDocument\x12\x36\n\x17open_document_filepaths\x18\x02 \x03(\tR\x15openDocumentFilepaths\x12\'\n\x0fworkspace_paths\x18\x03 \x03(\tR\x0eworkspacePaths\x12\x1a\n\x08\x62locking\x18\x04 \x01(\x08R\x08\x62locking\"$\n\"RefreshContextForIdeActionResponse\"S\n\x13GetFunctionsRequest\x12<\n\x08\x64ocument\x18\x01 \x01(\x0b\x32 .exa.language_server_pb.DocumentR\x08\x64ocument\"h\n\x14GetFunctionsResponse\x12P\n\x11\x66unction_captures\x18\x01 \x03(\x0b\x32#.exa.codeium_common_pb.FunctionInfoR\x10\x66unctionCaptures\"S\n\x14GetUserStatusRequest\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32\x1f.exa.codeium_common_pb.MetadataR\x08metadata\"[\n\x15GetUserStatusResponse\x12\x42\n\x0buser_status\x18\x01 \x01(\x0b\x32!.exa.codeium_common_pb.UserStatusR\nuserStatus\"6\n\x10\x44ocumentPosition\x12\x10\n\x03row\x18\x01 \x01(\x04R\x03row\x12\x10\n\x03\x63ol\x18\x02 \x01(\x04R\x03\x63ol\"\xab\x03\n\x08\x44ocument\x12#\n\rabsolute_path\x18\x01 \x01(\tR\x0c\x61\x62solutePath\x12#\n\rrelative_path\x18\x02 \x01(\tR\x0crelativePath\x12\x12\n\x04text\x18\x03 \x01(\tR\x04text\x12\'\n\x0f\x65\x64itor_language\x18\x04 \x01(\tR\x0e\x65\x64itorLanguage\x12;\n\x08language\x18\x05 \x01(\x0e\x32\x1f.exa.codeium_common_pb.LanguageR\x08language\x12#\n\rcursor_offset\x18\x06 \x01(\x04R\x0c\x63ursorOffset\x12Q\n\x0f\x63ursor_position\x18\x08 \x01(\x0b\x32(.exa.language_server_pb.DocumentPositionR\x0e\x63ursorPosition\x12\x1f\n\x0bline_ending\x18\x07 \x01(\tR\nlineEnding\x12\x42\n\rvisible_range\x18\t \x01(\x0b\x32\x1d.exa.language_server_pb.RangeR\x0cvisibleRange\"O\n\rEditorOptions\x12\x19\n\x08tab_size\x18\x01 \x01(\x04R\x07tabSize\x12#\n\rinsert_spaces\x18\x02 \x01(\x08R\x0cinsertSpaces\"]\n\x05State\x12:\n\x05state\x18\x01 \x01(\x0e\x32$.exa.language_server_pb.CodeiumStateR\x05state\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"\xe7\x01\n\x05Range\x12!\n\x0cstart_offset\x18\x01 \x01(\x04R\x0bstartOffset\x12\x1d\n\nend_offset\x18\x02 \x01(\x04R\tendOffset\x12O\n\x0estart_position\x18\x03 \x01(\x0b\x32(.exa.language_server_pb.DocumentPositionR\rstartPosition\x12K\n\x0c\x65nd_position\x18\x04 \x01(\x0b\x32(.exa.language_server_pb.DocumentPositionR\x0b\x65ndPosition\"L\n\x06Suffix\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12.\n\x13\x64\x65lta_cursor_offset\x18\x02 \x01(\x03R\x11\x64\x65ltaCursorOffset\"\xa8\x01\n\x0e\x43ompletionPart\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x16\n\x06offset\x18\x02 \x01(\x04R\x06offset\x12>\n\x04type\x18\x03 \x01(\x0e\x32*.exa.language_server_pb.CompletionPartTypeR\x04type\x12\x16\n\x06prefix\x18\x04 \x01(\tR\x06prefix\x12\x12\n\x04line\x18\x05 \x01(\x04R\x04line\"\xd4\x02\n\x0e\x43ompletionItem\x12\x41\n\ncompletion\x18\x01 \x01(\x0b\x32!.exa.codeium_common_pb.CompletionR\ncompletion\x12\x36\n\x06suffix\x18\x05 \x01(\x0b\x32\x1e.exa.language_server_pb.SuffixR\x06suffix\x12\x33\n\x05range\x18\x02 \x01(\x0b\x32\x1d.exa.language_server_pb.RangeR\x05range\x12?\n\x06source\x18\x03 \x01(\x0e\x32\'.exa.codeium_common_pb.CompletionSourceR\x06source\x12Q\n\x10\x63ompletion_parts\x18\x08 \x03(\x0b\x32&.exa.language_server_pb.CompletionPartR\x0f\x63ompletionParts\"\xd4\x01\n\x10\x45xperimentConfig\x12^\n\x18\x66orce_enable_experiments\x18\x01 \x03(\x0e\x32$.exa.codeium_common_pb.ExperimentKeyR\x16\x66orceEnableExperiments\x12`\n\x19\x66orce_disable_experiments\x18\x02 \x03(\x0e\x32$.exa.codeium_common_pb.ExperimentKeyR\x17\x66orceDisableExperiments\"\xfd\x02\n\x0cSearchResult\x12!\n\x0c\x65mbedding_id\x18\x01 \x01(\x03R\x0b\x65mbeddingId\x12#\n\rabsolute_path\x18\x02 \x01(\tR\x0c\x61\x62solutePath\x12M\n\x0fworkspace_paths\x18\x03 \x03(\x0b\x32$.exa.codeium_common_pb.WorkspacePathR\x0eworkspacePaths\x12W\n\x12\x65mbedding_metadata\x18\x04 \x01(\x0b\x32(.exa.codeium_common_pb.EmbeddingMetadataR\x11\x65mbeddingMetadata\x12)\n\x10similarity_score\x18\x05 \x01(\x02R\x0fsimilarityScore\x12R\n\x11\x63ode_context_item\x18\x06 \x01(\x0b\x32&.exa.codeium_common_pb.CodeContextItemR\x0f\x63odeContextItem\"\xa3\x02\n\x13SearchResultCluster\x12K\n\x0esearch_results\x18\x01 \x03(\x0b\x32$.exa.language_server_pb.SearchResultR\rsearchResults\x12/\n\x13representative_path\x18\x02 \x01(\tR\x12representativePath\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x32\n\x15mean_similarity_score\x18\x04 \x01(\x02R\x13meanSimilarityScore\x12\x1b\n\tsearch_id\x18\x05 \x01(\tR\x08searchId\x12\x1b\n\tresult_id\x18\x06 \x01(\tR\x08resultId\"U\n\x0bProgressBar\x12\x1a\n\x08progress\x18\x01 \x01(\x02R\x08progress\x12\x12\n\x04text\x18\x02 \x01(\tR\x04text\x12\x16\n\x06hidden\x18\x03 \x01(\x08R\x06hidden\"\xbd\x01\n\x10\x45xactSearchQuery\x12\x18\n\x07pattern\x18\x01 \x01(\tR\x07pattern\x12!\n\x0cis_multiline\x18\x02 \x01(\x08R\x0bisMultiline\x12\x1c\n\nis_reg_exp\x18\x03 \x01(\x08R\x08isRegExp\x12*\n\x11is_case_sensitive\x18\x04 \x01(\x08R\x0fisCaseSensitive\x12\"\n\ris_word_match\x18\x05 \x01(\x08R\x0bisWordMatch\"\xe8\x04\n\x12\x45xactSearchOptions\x12\x16\n\x06\x66older\x18\x01 \x01(\tR\x06\x66older\x12\x1a\n\x08includes\x18\x02 \x03(\tR\x08includes\x12\x1a\n\x08\x65xcludes\x18\x03 \x03(\tR\x08\x65xcludes\x12\x34\n\x16\x64isregard_ignore_files\x18\x04 \x01(\x08R\x14\x64isregardIgnoreFiles\x12\'\n\x0f\x66ollow_symlinks\x18\x05 \x01(\x08R\x0e\x66ollowSymlinks\x12\x41\n\x1d\x64isregard_global_ignore_files\x18\x06 \x01(\x08R\x1a\x64isregardGlobalIgnoreFiles\x12\x41\n\x1d\x64isregard_parent_ignore_files\x18\x07 \x01(\x08R\x1a\x64isregardParentIgnoreFiles\x12\"\n\rmax_file_size\x18\x08 \x01(\rR\x0bmaxFileSize\x12\x1a\n\x08\x65ncoding\x18\t \x01(\tR\x08\x65ncoding\x12\x30\n\x14\x62\x65\x66ore_context_lines\x18\n \x01(\rR\x12\x62\x65\x66oreContextLines\x12.\n\x13\x61\x66ter_context_lines\x18\x0b \x01(\rR\x11\x61\x66terContextLines\x12\x1f\n\x0bmax_results\x18\x0c \x01(\rR\nmaxResults\x12Z\n\x0fpreview_options\x18\r \x01(\x0b\x32\x31.exa.language_server_pb.ExactSearchPreviewOptionsR\x0epreviewOptions\"b\n\x19\x45xactSearchPreviewOptions\x12\x1f\n\x0bmatch_lines\x18\x01 \x01(\rR\nmatchLines\x12$\n\x0e\x63hars_per_line\x18\x02 \x01(\rR\x0c\x63harsPerLine\"\xfc\x01\n\x11\x45xactSearchResult\x12#\n\rabsolute_path\x18\x01 \x01(\tR\x0c\x61\x62solutePath\x12#\n\rrelative_path\x18\x04 \x01(\tR\x0crelativePath\x12\x35\n\x06ranges\x18\x02 \x03(\x0b\x32\x1d.exa.language_server_pb.RangeR\x06ranges\x12I\n\x07preview\x18\x03 \x01(\x0b\x32/.exa.language_server_pb.ExactSearchMatchPreviewR\x07preview\x12\x1b\n\tresult_id\x18\x05 \x01(\tR\x08resultId\"d\n\x17\x45xactSearchMatchPreview\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x35\n\x06ranges\x18\x02 \x03(\x0b\x32\x1d.exa.language_server_pb.RangeR\x06ranges*\xb6\x01\n\x0c\x43odeiumState\x12\x1d\n\x19\x43ODEIUM_STATE_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x43ODEIUM_STATE_INACTIVE\x10\x01\x12\x1c\n\x18\x43ODEIUM_STATE_PROCESSING\x10\x02\x12\x19\n\x15\x43ODEIUM_STATE_SUCCESS\x10\x03\x12\x19\n\x15\x43ODEIUM_STATE_WARNING\x10\x04\x12\x17\n\x13\x43ODEIUM_STATE_ERROR\x10\x05*P\n\x08LineType\x12\x19\n\x15LINE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10LINE_TYPE_SINGLE\x10\x01\x12\x13\n\x0fLINE_TYPE_MULTI\x10\x02*\xa1\x01\n\x12\x43ompletionPartType\x12$\n COMPLETION_PART_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x43OMPLETION_PART_TYPE_INLINE\x10\x01\x12\x1e\n\x1a\x43OMPLETION_PART_TYPE_BLOCK\x10\x02\x12$\n COMPLETION_PART_TYPE_INLINE_MASK\x10\x03\x32\xd4\x10\n\x15LanguageServerService\x12q\n\x0eGetCompletions\x12-.exa.language_server_pb.GetCompletionsRequest\x1a..exa.language_server_pb.GetCompletionsResponse\"\x00\x12w\n\x10\x41\x63\x63\x65ptCompletion\x12/.exa.language_server_pb.AcceptCompletionRequest\x1a\x30.exa.language_server_pb.AcceptCompletionResponse\"\x00\x12\x62\n\tHeartbeat\x12(.exa.language_server_pb.HeartbeatRequest\x1a).exa.language_server_pb.HeartbeatResponse\"\x00\x12k\n\x0cGetAuthToken\x12+.exa.language_server_pb.GetAuthTokenRequest\x1a,.exa.language_server_pb.GetAuthTokenResponse\"\x00\x12h\n\x0bRecordEvent\x12*.exa.language_server_pb.RecordEventRequest\x1a+.exa.language_server_pb.RecordEventResponse\"\x00\x12n\n\rCancelRequest\x12,.exa.language_server_pb.CancelRequestRequest\x1a-.exa.language_server_pb.CancelRequestResponse\"\x00\x12S\n\x04\x45xit\x12#.exa.language_server_pb.ExitRequest\x1a$.exa.language_server_pb.ExitResponse\"\x00\x12k\n\x0cGetProcesses\x12+.exa.language_server_pb.GetProcessesRequest\x1a,.exa.language_server_pb.GetProcessesResponse\"\x00\x12s\n\x0eGetChatMessage\x12-.exa.language_server_pb.GetChatMessageRequest\x1a..exa.language_server_pb.GetChatMessageResponse\"\x00\x30\x01\x12}\n\x12RecordChatFeedback\x12\x31.exa.language_server_pb.RecordChatFeedbackRequest\x1a\x32.exa.language_server_pb.RecordChatFeedbackResponse\"\x00\x12\x89\x01\n\x16RecordChatPanelSession\x12\x35.exa.language_server_pb.RecordChatPanelSessionRequest\x1a\x36.exa.language_server_pb.RecordChatPanelSessionResponse\"\x00\x12t\n\x0f\x43lusteredSearch\x12..exa.language_server_pb.ClusteredSearchRequest\x1a/.exa.language_server_pb.ClusteredSearchResponse\"\x00\x12h\n\x0b\x45xactSearch\x12*.exa.language_server_pb.ExactSearchRequest\x1a+.exa.language_server_pb.ExactSearchResponse\"\x00\x12\x80\x01\n\x13\x41\x64\x64TrackedWorkspace\x12\x32.exa.language_server_pb.AddTrackedWorkspaceRequest\x1a\x33.exa.language_server_pb.AddTrackedWorkspaceResponse\"\x00\x12\x89\x01\n\x16RemoveTrackedWorkspace\x12\x35.exa.language_server_pb.RemoveTrackedWorkspaceRequest\x1a\x36.exa.language_server_pb.RemoveTrackedWorkspaceResponse\"\x00\x12\x95\x01\n\x1aRefreshContextForIdeAction\x12\x39.exa.language_server_pb.RefreshContextForIdeActionRequest\x1a:.exa.language_server_pb.RefreshContextForIdeActionResponse\"\x00\x12k\n\x0cGetFunctions\x12+.exa.language_server_pb.GetFunctionsRequest\x1a,.exa.language_server_pb.GetFunctionsResponse\"\x00\x12n\n\rGetUserStatus\x12,.exa.language_server_pb.GetUserStatusRequest\x1a-.exa.language_server_pb.GetUserStatusResponse\"\x00\x42\xdd\x01\n\x1a\x63om.exa.language_server_pbB\x13LanguageServerProtoP\x01Z9github.com/Exafunction/Exafunction/exa/language_server_pb\xa2\x02\x03\x45LX\xaa\x02\x14\x45xa.LanguageServerPb\xca\x02\x14\x45xa\\LanguageServerPb\xe2\x02 Exa\\LanguageServerPb\\GPBMetadata\xea\x02\x15\x45xa::LanguageServerPbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exa.language_server_pb.language_server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.exa.language_server_pbB\023LanguageServerProtoP\001Z9github.com/Exafunction/Exafunction/exa/language_server_pb\242\002\003ELX\252\002\024Exa.LanguageServerPb\312\002\024Exa\\LanguageServerPb\342\002 Exa\\LanguageServerPb\\GPBMetadata\352\002\025Exa::LanguageServerPb'
  _globals['_CODEIUMSTATE']._serialized_start=7931
  _globals['_CODEIUMSTATE']._serialized_end=8113
  _globals['_LINETYPE']._serialized_start=8115
  _globals['_LINETYPE']._serialized_end=8195
  _globals['_COMPLETIONPARTTYPE']._serialized_start=8198
  _globals['_COMPLETIONPARTTYPE']._serialized_end=8359
  _globals['_GETCOMPLETIONSREQUEST']._serialized_start=174
  _globals['_GETCOMPLETIONSREQUEST']._serialized_end=503
  _globals['_GETCOMPLETIONSRESPONSE']._serialized_start=506
  _globals['_GETCOMPLETIONSRESPONSE']._serialized_end=666
  _globals['_ACCEPTCOMPLETIONREQUEST']._serialized_start=668
  _globals['_ACCEPTCOMPLETIONREQUEST']._serialized_end=791
  _globals['_ACCEPTCOMPLETIONRESPONSE']._serialized_start=793
  _globals['_ACCEPTCOMPLETIONRESPONSE']._serialized_end=819
  _globals['_HEARTBEATREQUEST']._serialized_start=821
  _globals['_HEARTBEATREQUEST']._serialized_end=900
  _globals['_HEARTBEATRESPONSE']._serialized_start=902
  _globals['_HEARTBEATRESPONSE']._serialized_end=921
  _globals['_GETAUTHTOKENREQUEST']._serialized_start=923
  _globals['_GETAUTHTOKENREQUEST']._serialized_end=944
  _globals['_GETAUTHTOKENRESPONSE']._serialized_start=946
  _globals['_GETAUTHTOKENRESPONSE']._serialized_end=1019
  _globals['_RECORDEVENTREQUEST']._serialized_start=1022
  _globals['_RECORDEVENTREQUEST']._serialized_end=1155
  _globals['_RECORDEVENTRESPONSE']._serialized_start=1157
  _globals['_RECORDEVENTRESPONSE']._serialized_end=1178
  _globals['_CANCELREQUESTREQUEST']._serialized_start=1180
  _globals['_CANCELREQUESTREQUEST']._serialized_end=1294
  _globals['_CANCELREQUESTRESPONSE']._serialized_start=1296
  _globals['_CANCELREQUESTRESPONSE']._serialized_end=1319
  _globals['_EXITREQUEST']._serialized_start=1321
  _globals['_EXITREQUEST']._serialized_end=1334
  _globals['_EXITRESPONSE']._serialized_start=1336
  _globals['_EXITRESPONSE']._serialized_end=1350
  _globals['_GETPROCESSESREQUEST']._serialized_start=1352
  _globals['_GETPROCESSESREQUEST']._serialized_end=1373
  _globals['_GETPROCESSESRESPONSE']._serialized_start=1376
  _globals['_GETPROCESSESRESPONSE']._serialized_end=1516
  _globals['_GETCHATMESSAGEREQUEST']._serialized_start=1519
  _globals['_GETCHATMESSAGEREQUEST']._serialized_end=2040
  _globals['_GETCHATMESSAGERESPONSE']._serialized_start=2042
  _globals['_GETCHATMESSAGERESPONSE']._serialized_end=2127
  _globals['_RECORDCHATFEEDBACKREQUEST']._serialized_start=2130
  _globals['_RECORDCHATFEEDBACKREQUEST']._serialized_end=2390
  _globals['_RECORDCHATFEEDBACKRESPONSE']._serialized_start=2392
  _globals['_RECORDCHATFEEDBACKRESPONSE']._serialized_end=2420
  _globals['_RECORDCHATPANELSESSIONREQUEST']._serialized_start=2423
  _globals['_RECORDCHATPANELSESSIONREQUEST']._serialized_end=2649
  _globals['_RECORDCHATPANELSESSIONRESPONSE']._serialized_start=2651
  _globals['_RECORDCHATPANELSESSIONRESPONSE']._serialized_end=2683
  _globals['_CLUSTEREDSEARCHREQUEST']._serialized_start=2686
  _globals['_CLUSTEREDSEARCHREQUEST']._serialized_end=2861
  _globals['_CLUSTEREDSEARCHRESPONSE']._serialized_start=2863
  _globals['_CLUSTEREDSEARCHRESPONSE']._serialized_end=2990
  _globals['_EXACTSEARCHREQUEST']._serialized_start=2993
  _globals['_EXACTSEARCHREQUEST']._serialized_end=3208
  _globals['_EXACTSEARCHRESPONSE']._serialized_start=3211
  _globals['_EXACTSEARCHRESPONSE']._serialized_end=3359
  _globals['_ADDTRACKEDWORKSPACEREQUEST']._serialized_start=3361
  _globals['_ADDTRACKEDWORKSPACEREQUEST']._serialized_end=3419
  _globals['_ADDTRACKEDWORKSPACERESPONSE']._serialized_start=3421
  _globals['_ADDTRACKEDWORKSPACERESPONSE']._serialized_end=3450
  _globals['_REMOVETRACKEDWORKSPACEREQUEST']._serialized_start=3452
  _globals['_REMOVETRACKEDWORKSPACEREQUEST']._serialized_end=3513
  _globals['_REMOVETRACKEDWORKSPACERESPONSE']._serialized_start=3515
  _globals['_REMOVETRACKEDWORKSPACERESPONSE']._serialized_end=3547
  _globals['_REFRESHCONTEXTFORIDEACTIONREQUEST']._serialized_start=3550
  _globals['_REFRESHCONTEXTFORIDEACTIONREQUEST']._serialized_end=3785
  _globals['_REFRESHCONTEXTFORIDEACTIONRESPONSE']._serialized_start=3787
  _globals['_REFRESHCONTEXTFORIDEACTIONRESPONSE']._serialized_end=3823
  _globals['_GETFUNCTIONSREQUEST']._serialized_start=3825
  _globals['_GETFUNCTIONSREQUEST']._serialized_end=3908
  _globals['_GETFUNCTIONSRESPONSE']._serialized_start=3910
  _globals['_GETFUNCTIONSRESPONSE']._serialized_end=4014
  _globals['_GETUSERSTATUSREQUEST']._serialized_start=4016
  _globals['_GETUSERSTATUSREQUEST']._serialized_end=4099
  _globals['_GETUSERSTATUSRESPONSE']._serialized_start=4101
  _globals['_GETUSERSTATUSRESPONSE']._serialized_end=4192
  _globals['_DOCUMENTPOSITION']._serialized_start=4194
  _globals['_DOCUMENTPOSITION']._serialized_end=4248
  _globals['_DOCUMENT']._serialized_start=4251
  _globals['_DOCUMENT']._serialized_end=4678
  _globals['_EDITOROPTIONS']._serialized_start=4680
  _globals['_EDITOROPTIONS']._serialized_end=4759
  _globals['_STATE']._serialized_start=4761
  _globals['_STATE']._serialized_end=4854
  _globals['_RANGE']._serialized_start=4857
  _globals['_RANGE']._serialized_end=5088
  _globals['_SUFFIX']._serialized_start=5090
  _globals['_SUFFIX']._serialized_end=5166
  _globals['_COMPLETIONPART']._serialized_start=5169
  _globals['_COMPLETIONPART']._serialized_end=5337
  _globals['_COMPLETIONITEM']._serialized_start=5340
  _globals['_COMPLETIONITEM']._serialized_end=5680
  _globals['_EXPERIMENTCONFIG']._serialized_start=5683
  _globals['_EXPERIMENTCONFIG']._serialized_end=5895
  _globals['_SEARCHRESULT']._serialized_start=5898
  _globals['_SEARCHRESULT']._serialized_end=6279
  _globals['_SEARCHRESULTCLUSTER']._serialized_start=6282
  _globals['_SEARCHRESULTCLUSTER']._serialized_end=6573
  _globals['_PROGRESSBAR']._serialized_start=6575
  _globals['_PROGRESSBAR']._serialized_end=6660
  _globals['_EXACTSEARCHQUERY']._serialized_start=6663
  _globals['_EXACTSEARCHQUERY']._serialized_end=6852
  _globals['_EXACTSEARCHOPTIONS']._serialized_start=6855
  _globals['_EXACTSEARCHOPTIONS']._serialized_end=7471
  _globals['_EXACTSEARCHPREVIEWOPTIONS']._serialized_start=7473
  _globals['_EXACTSEARCHPREVIEWOPTIONS']._serialized_end=7571
  _globals['_EXACTSEARCHRESULT']._serialized_start=7574
  _globals['_EXACTSEARCHRESULT']._serialized_end=7826
  _globals['_EXACTSEARCHMATCHPREVIEW']._serialized_start=7828
  _globals['_EXACTSEARCHMATCHPREVIEW']._serialized_end=7928
  _globals['_LANGUAGESERVERSERVICE']._serialized_start=8362
  _globals['_LANGUAGESERVERSERVICE']._serialized_end=10494
# @@protoc_insertion_point(module_scope)
