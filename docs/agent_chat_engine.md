# Agent Chat Engine Service API 说明

## 服务概述

`AgentChatEngineService` 提供与聊天代理相关的功能。该服务支持两种调用方式：

1. **Call**：用于发起一次性请求并返回响应。
2. **StreamCall**：用于发起请求并接收流式响应。

## API 方法

### 1. Call 方法

**描述**  
`Call` 方法用于发起单次对话请求，并返回单个响应。

**请求**

- **CallRequest**

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 请求的唯一标识符。             |
| `agent`       | `microcommon.v1.Resource`     | 用于标识代理的信息。          |
| `query`       | `string`                     | 用户提出的查询内容。          |
| `history`     | `repeated HistoryMessage`     | 历史消息记录，提供上下文。    |

- **HistoryMessage**

| 字段名        | 类型     | 描述                          |
| ------------- | -------- | ----------------------------- |
| `query`       | `string` | 用户提出的历史查询内容。      |
| `answer`      | `string` | 代理提供的历史回答内容。      |

**响应**

- **CallResponse**

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 请求的唯一标识符。             |
| `answer`      | `string`                     | 代理的回答。                  |
| `latency`     | `int64`                      | 响应延迟时间，单位为毫秒。    |
| `created_at`  | `google.protobuf.Timestamp`   | 响应创建的时间戳。            |

---

### 2. StreamCall 方法

**描述**  
`StreamCall` 方法用于发起流式对话请求，并接收多个响应，适合需要多轮交互的场景。

**请求**

- **StreamCallRequest**

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 请求的唯一标识符。             |
| `agent`       | `microcommon.v1.Resource`     | 用于标识代理的信息。          |
| `query`       | `string`                     | 用户提出的查询内容。          |
| `history`     | `repeated HistoryMessage`     | 历史消息记录，提供上下文。    |
| `show_debug`  | `bool`                       | 是否显示调试信息。            |

**响应**

- **StreamCallResponse**

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 响应的唯一标识符。             |
| `answer`      | `string`                     | 代理的回答。                  |
| `latency`     | `int64`                      | 响应延迟时间，单位为毫秒。    |
| `created_at`  | `google.protobuf.Timestamp`   | 响应创建的时间戳。            |

---

## 数据结构

### HistoryMessage

**描述**  
`HistoryMessage` 用于表示历史消息记录，包含用户的历史查询及代理的历史回答。

| 字段名        | 类型     | 描述                          |
| ------------- | -------- | ----------------------------- |
| `query`       | `string` | 用户提出的历史查询内容。      |
| `answer`      | `string` | 代理提供的历史回答内容。      |

### CallRequest

**描述**  
`CallRequest` 用于表示一次对话请求。

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 请求的唯一标识符。             |
| `agent`       | `microcommon.v1.Resource`     | 用于标识代理的信息。          |
| `query`       | `string`                     | 用户提出的查询内容。          |
| `history`     | `repeated HistoryMessage`     | 历史消息记录，提供上下文。    |

### CallResponse

**描述**  
`CallResponse` 用于表示对话请求的响应结果。

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 请求的唯一标识符。             |
| `answer`      | `string`                     | 代理的回答。                  |
| `latency`     | `int64`                      | 响应延迟时间，单位为毫秒。    |
| `created_at`  | `google.protobuf.Timestamp`   | 响应创建的时间戳。            |

### StreamCallRequest

**描述**  
`StreamCallRequest` 用于表示一次流式对话请求。

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 请求的唯一标识符。             |
| `agent`       | `microcommon.v1.Resource`     | 用于标识代理的信息。          |
| `query`       | `string`                     | 用户提出的查询内容。          |
| `history`     | `repeated HistoryMessage`     | 历史消息记录，提供上下文。    |
| `show_debug`  | `bool`                       | 是否显示调试信息。            |

### StreamCallResponse

**描述**  
`StreamCallResponse` 用于表示流式对话请求的响应结果。

| 字段名        | 类型                         | 描述                          |
| ------------- | ---------------------------- | ----------------------------- |
| `id`          | `string`                     | 响应的唯一标识符。             |
| `answer`      | `string`                     | 代理的回答。                  |
| `latency`     | `int64`                      | 响应延迟时间，单位为毫秒。    |
| `created_at`  | `google.protobuf.Timestamp`   | 响应创建的时间戳。            |
