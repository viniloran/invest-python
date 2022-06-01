# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/marketdata.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tinkoff.invest.grpc import common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$tinkoff/invest/grpc/marketdata.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a tinkoff/invest/grpc/common.proto\"\x99\x04\n\x11MarketDataRequest\x12\x63\n\x19subscribe_candles_request\x18\x01 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequestH\x00\x12h\n\x1csubscribe_order_book_request\x18\x02 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequestH\x00\x12\x61\n\x18subscribe_trades_request\x18\x03 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.SubscribeTradesRequestH\x00\x12]\n\x16subscribe_info_request\x18\x04 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscribeInfoRequestH\x00\x12h\n\x1csubscribe_last_price_request\x18\x05 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequestH\x00\x42\t\n\x07payload\"\x94\x04\n!MarketDataServerSideStreamRequest\x12\x61\n\x19subscribe_candles_request\x18\x01 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequest\x12\x66\n\x1csubscribe_order_book_request\x18\x02 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequest\x12_\n\x18subscribe_trades_request\x18\x03 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.SubscribeTradesRequest\x12[\n\x16subscribe_info_request\x18\x04 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscribeInfoRequest\x12\x66\n\x1csubscribe_last_price_request\x18\x05 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequest\"\xc0\x07\n\x12MarketDataResponse\x12\x65\n\x1asubscribe_candles_response\x18\x01 \x01(\x0b\x32?.tinkoff.public.invest.api.contract.v1.SubscribeCandlesResponseH\x00\x12j\n\x1dsubscribe_order_book_response\x18\x02 \x01(\x0b\x32\x41.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookResponseH\x00\x12\x63\n\x19subscribe_trades_response\x18\x03 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeTradesResponseH\x00\x12_\n\x17subscribe_info_response\x18\x04 \x01(\x0b\x32<.tinkoff.public.invest.api.contract.v1.SubscribeInfoResponseH\x00\x12?\n\x06\x63\x61ndle\x18\x05 \x01(\x0b\x32-.tinkoff.public.invest.api.contract.v1.CandleH\x00\x12=\n\x05trade\x18\x06 \x01(\x0b\x32,.tinkoff.public.invest.api.contract.v1.TradeH\x00\x12\x45\n\torderbook\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.OrderBookH\x00\x12N\n\x0etrading_status\x18\x08 \x01(\x0b\x32\x34.tinkoff.public.invest.api.contract.v1.TradingStatusH\x00\x12;\n\x04ping\x18\t \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x12j\n\x1dsubscribe_last_price_response\x18\n \x01(\x0b\x32\x41.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceResponseH\x00\x12\x46\n\nlast_price\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.LastPriceH\x00\x42\t\n\x07payload\"\xd6\x01\n\x17SubscribeCandlesRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12L\n\x0binstruments\x18\x02 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.CandleInstrument\x12\x15\n\rwaiting_close\x18\x03 \x01(\x08\"o\n\x10\x43\x61ndleInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\"\x89\x01\n\x18SubscribeCandlesResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12X\n\x15\x63\x61ndles_subscriptions\x18\x02 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.CandleSubscription\"\xc9\x01\n\x12\x43\x61ndleSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12V\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\"\xc4\x01\n\x19SubscribeOrderBookRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12O\n\x0binstruments\x18\x02 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.OrderBookInstrument\"2\n\x13OrderBookInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\"\x91\x01\n\x1aSubscribeOrderBookResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12^\n\x18order_book_subscriptions\x18\x02 \x03(\x0b\x32<.tinkoff.public.invest.api.contract.v1.OrderBookSubscription\"\x8c\x01\n\x15OrderBookSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12V\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\"\xbd\x01\n\x16SubscribeTradesRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12K\n\x0binstruments\x18\x02 \x03(\x0b\x32\x36.tinkoff.public.invest.api.contract.v1.TradeInstrument\"\x1f\n\x0fTradeInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\"\x85\x01\n\x17SubscribeTradesResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12U\n\x13trade_subscriptions\x18\x02 \x03(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.TradeSubscription\"y\n\x11TradeSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\"\xba\x01\n\x14SubscribeInfoRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12J\n\x0binstruments\x18\x02 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.InfoInstrument\"\x1e\n\x0eInfoInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\"\x81\x01\n\x15SubscribeInfoResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12S\n\x12info_subscriptions\x18\x02 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.InfoSubscription\"x\n\x10InfoSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\"\xc4\x01\n\x19SubscribeLastPriceRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12O\n\x0binstruments\x18\x02 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.LastPriceInstrument\"#\n\x13LastPriceInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\"\x91\x01\n\x1aSubscribeLastPriceResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12^\n\x18last_price_subscriptions\x18\x02 \x03(\x0b\x32<.tinkoff.public.invest.api.contract.v1.LastPriceSubscription\"}\n\x15LastPriceSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\"\xd2\x03\n\x06\x43\x61ndle\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12>\n\x04open\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12>\n\x04high\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03low\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12?\n\x05\x63lose\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0e\n\x06volume\x18\x07 \x01(\x03\x12(\n\x04time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rlast_trade_ts\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xeb\x02\n\tOrderBook\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x15\n\ris_consistent\x18\x03 \x01(\x08\x12:\n\x04\x62ids\x18\x04 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12:\n\x04\x61sks\x18\x05 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x08limit_up\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nlimit_down\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"Z\n\x05Order\x12?\n\x05price\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x02 \x01(\x03\"\xdc\x01\n\x05Trade\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12H\n\tdirection\x18\x02 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.TradeDirection\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x04 \x01(\x03\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe6\x01\n\rTradingStatus\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12T\n\x0etrading_status\x18\x02 \x01(\x0e\x32<.tinkoff.public.invest.api.contract.v1.SecurityTradingStatus\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x1alimit_order_available_flag\x18\x04 \x01(\x08\x12#\n\x1bmarket_order_available_flag\x18\x05 \x01(\x08\"\xbc\x01\n\x11GetCandlesRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x08interval\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.CandleInterval\"\\\n\x12GetCandlesResponse\x12\x46\n\x07\x63\x61ndles\x18\x01 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.HistoricCandle\"\xdf\x02\n\x0eHistoricCandle\x12>\n\x04open\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12>\n\x04high\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03low\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12?\n\x05\x63lose\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0e\n\x06volume\x18\x05 \x01(\x03\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bis_complete\x18\x07 \x01(\x08\"$\n\x14GetLastPricesRequest\x12\x0c\n\x04\x66igi\x18\x01 \x03(\t\"^\n\x15GetLastPricesResponse\x12\x45\n\x0blast_prices\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.LastPrice\"\x84\x01\n\tLastPrice\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x13GetOrderBookRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\"\xc2\x03\n\x14GetOrderBookResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12:\n\x04\x62ids\x18\x03 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12:\n\x04\x61sks\x18\x04 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12\x44\n\nlast_price\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x45\n\x0b\x63lose_price\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x42\n\x08limit_up\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nlimit_down\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"\'\n\x17GetTradingStatusRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\"\xe9\x01\n\x18GetTradingStatusResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12T\n\x0etrading_status\x18\x02 \x01(\x0e\x32<.tinkoff.public.invest.api.contract.v1.SecurityTradingStatus\x12\"\n\x1alimit_order_available_flag\x18\x03 \x01(\x08\x12#\n\x1bmarket_order_available_flag\x18\x04 \x01(\x08\x12 \n\x18\x61pi_trade_available_flag\x18\x05 \x01(\x08\"v\n\x14GetLastTradesRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"U\n\x15GetLastTradesResponse\x12<\n\x06trades\x18\x01 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Trade*\x81\x01\n\x12SubscriptionAction\x12#\n\x1fSUBSCRIPTION_ACTION_UNSPECIFIED\x10\x00\x12!\n\x1dSUBSCRIPTION_ACTION_SUBSCRIBE\x10\x01\x12#\n\x1fSUBSCRIPTION_ACTION_UNSUBSCRIBE\x10\x02*\x8b\x01\n\x14SubscriptionInterval\x12%\n!SUBSCRIPTION_INTERVAL_UNSPECIFIED\x10\x00\x12$\n SUBSCRIPTION_INTERVAL_ONE_MINUTE\x10\x01\x12&\n\"SUBSCRIPTION_INTERVAL_FIVE_MINUTES\x10\x02*\x95\x03\n\x12SubscriptionStatus\x12#\n\x1fSUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12,\n(SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND\x10\x02\x12\x36\n2SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID\x10\x03\x12(\n$SUBSCRIPTION_STATUS_DEPTH_IS_INVALID\x10\x04\x12+\n\'SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID\x10\x05\x12)\n%SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED\x10\x06\x12&\n\"SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x07\x12)\n%SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS\x10\x08*d\n\x0eTradeDirection\x12\x1f\n\x1bTRADE_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13TRADE_DIRECTION_BUY\x10\x01\x12\x18\n\x14TRADE_DIRECTION_SELL\x10\x02*\xb6\x01\n\x0e\x43\x61ndleInterval\x12\x1f\n\x1b\x43\x41NDLE_INTERVAL_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43\x41NDLE_INTERVAL_1_MIN\x10\x01\x12\x19\n\x15\x43\x41NDLE_INTERVAL_5_MIN\x10\x02\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_15_MIN\x10\x03\x12\x18\n\x14\x43\x41NDLE_INTERVAL_HOUR\x10\x04\x12\x17\n\x13\x43\x41NDLE_INTERVAL_DAY\x10\x05\x32\xd1\x05\n\x11MarketDataService\x12\x81\x01\n\nGetCandles\x12\x38.tinkoff.public.invest.api.contract.v1.GetCandlesRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.GetCandlesResponse\x12\x8a\x01\n\rGetLastPrices\x12;.tinkoff.public.invest.api.contract.v1.GetLastPricesRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetLastPricesResponse\x12\x87\x01\n\x0cGetOrderBook\x12:.tinkoff.public.invest.api.contract.v1.GetOrderBookRequest\x1a;.tinkoff.public.invest.api.contract.v1.GetOrderBookResponse\x12\x93\x01\n\x10GetTradingStatus\x12>.tinkoff.public.invest.api.contract.v1.GetTradingStatusRequest\x1a?.tinkoff.public.invest.api.contract.v1.GetTradingStatusResponse\x12\x8a\x01\n\rGetLastTrades\x12;.tinkoff.public.invest.api.contract.v1.GetLastTradesRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetLastTradesResponse2\xcd\x02\n\x17MarketDataStreamService\x12\x8b\x01\n\x10MarketDataStream\x12\x38.tinkoff.public.invest.api.contract.v1.MarketDataRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.MarketDataResponse(\x01\x30\x01\x12\xa3\x01\n\x1aMarketDataServerSideStream\x12H.tinkoff.public.invest.api.contract.v1.MarketDataServerSideStreamRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.MarketDataResponse0\x01\x42\x61\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_SUBSCRIPTIONACTION = DESCRIPTOR.enum_types_by_name['SubscriptionAction']
SubscriptionAction = enum_type_wrapper.EnumTypeWrapper(_SUBSCRIPTIONACTION)
_SUBSCRIPTIONINTERVAL = DESCRIPTOR.enum_types_by_name['SubscriptionInterval']
SubscriptionInterval = enum_type_wrapper.EnumTypeWrapper(_SUBSCRIPTIONINTERVAL)
_SUBSCRIPTIONSTATUS = DESCRIPTOR.enum_types_by_name['SubscriptionStatus']
SubscriptionStatus = enum_type_wrapper.EnumTypeWrapper(_SUBSCRIPTIONSTATUS)
_TRADEDIRECTION = DESCRIPTOR.enum_types_by_name['TradeDirection']
TradeDirection = enum_type_wrapper.EnumTypeWrapper(_TRADEDIRECTION)
_CANDLEINTERVAL = DESCRIPTOR.enum_types_by_name['CandleInterval']
CandleInterval = enum_type_wrapper.EnumTypeWrapper(_CANDLEINTERVAL)
SUBSCRIPTION_ACTION_UNSPECIFIED = 0
SUBSCRIPTION_ACTION_SUBSCRIBE = 1
SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2
SUBSCRIPTION_INTERVAL_UNSPECIFIED = 0
SUBSCRIPTION_INTERVAL_ONE_MINUTE = 1
SUBSCRIPTION_INTERVAL_FIVE_MINUTES = 2
SUBSCRIPTION_STATUS_UNSPECIFIED = 0
SUBSCRIPTION_STATUS_SUCCESS = 1
SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND = 2
SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID = 3
SUBSCRIPTION_STATUS_DEPTH_IS_INVALID = 4
SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID = 5
SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED = 6
SUBSCRIPTION_STATUS_INTERNAL_ERROR = 7
SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS = 8
TRADE_DIRECTION_UNSPECIFIED = 0
TRADE_DIRECTION_BUY = 1
TRADE_DIRECTION_SELL = 2
CANDLE_INTERVAL_UNSPECIFIED = 0
CANDLE_INTERVAL_1_MIN = 1
CANDLE_INTERVAL_5_MIN = 2
CANDLE_INTERVAL_15_MIN = 3
CANDLE_INTERVAL_HOUR = 4
CANDLE_INTERVAL_DAY = 5


_MARKETDATAREQUEST = DESCRIPTOR.message_types_by_name['MarketDataRequest']
_MARKETDATASERVERSIDESTREAMREQUEST = DESCRIPTOR.message_types_by_name['MarketDataServerSideStreamRequest']
_MARKETDATARESPONSE = DESCRIPTOR.message_types_by_name['MarketDataResponse']
_SUBSCRIBECANDLESREQUEST = DESCRIPTOR.message_types_by_name['SubscribeCandlesRequest']
_CANDLEINSTRUMENT = DESCRIPTOR.message_types_by_name['CandleInstrument']
_SUBSCRIBECANDLESRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeCandlesResponse']
_CANDLESUBSCRIPTION = DESCRIPTOR.message_types_by_name['CandleSubscription']
_SUBSCRIBEORDERBOOKREQUEST = DESCRIPTOR.message_types_by_name['SubscribeOrderBookRequest']
_ORDERBOOKINSTRUMENT = DESCRIPTOR.message_types_by_name['OrderBookInstrument']
_SUBSCRIBEORDERBOOKRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeOrderBookResponse']
_ORDERBOOKSUBSCRIPTION = DESCRIPTOR.message_types_by_name['OrderBookSubscription']
_SUBSCRIBETRADESREQUEST = DESCRIPTOR.message_types_by_name['SubscribeTradesRequest']
_TRADEINSTRUMENT = DESCRIPTOR.message_types_by_name['TradeInstrument']
_SUBSCRIBETRADESRESPONSE = DESCRIPTOR.message_types_by_name['SubscribeTradesResponse']
_TRADESUBSCRIPTION = DESCRIPTOR.message_types_by_name['TradeSubscription']
_SUBSCRIBEINFOREQUEST = DESCRIPTOR.message_types_by_name['SubscribeInfoRequest']
_INFOINSTRUMENT = DESCRIPTOR.message_types_by_name['InfoInstrument']
_SUBSCRIBEINFORESPONSE = DESCRIPTOR.message_types_by_name['SubscribeInfoResponse']
_INFOSUBSCRIPTION = DESCRIPTOR.message_types_by_name['InfoSubscription']
_SUBSCRIBELASTPRICEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeLastPriceRequest']
_LASTPRICEINSTRUMENT = DESCRIPTOR.message_types_by_name['LastPriceInstrument']
_SUBSCRIBELASTPRICERESPONSE = DESCRIPTOR.message_types_by_name['SubscribeLastPriceResponse']
_LASTPRICESUBSCRIPTION = DESCRIPTOR.message_types_by_name['LastPriceSubscription']
_CANDLE = DESCRIPTOR.message_types_by_name['Candle']
_ORDERBOOK = DESCRIPTOR.message_types_by_name['OrderBook']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_TRADE = DESCRIPTOR.message_types_by_name['Trade']
_TRADINGSTATUS = DESCRIPTOR.message_types_by_name['TradingStatus']
_GETCANDLESREQUEST = DESCRIPTOR.message_types_by_name['GetCandlesRequest']
_GETCANDLESRESPONSE = DESCRIPTOR.message_types_by_name['GetCandlesResponse']
_HISTORICCANDLE = DESCRIPTOR.message_types_by_name['HistoricCandle']
_GETLASTPRICESREQUEST = DESCRIPTOR.message_types_by_name['GetLastPricesRequest']
_GETLASTPRICESRESPONSE = DESCRIPTOR.message_types_by_name['GetLastPricesResponse']
_LASTPRICE = DESCRIPTOR.message_types_by_name['LastPrice']
_GETORDERBOOKREQUEST = DESCRIPTOR.message_types_by_name['GetOrderBookRequest']
_GETORDERBOOKRESPONSE = DESCRIPTOR.message_types_by_name['GetOrderBookResponse']
_GETTRADINGSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetTradingStatusRequest']
_GETTRADINGSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['GetTradingStatusResponse']
_GETLASTTRADESREQUEST = DESCRIPTOR.message_types_by_name['GetLastTradesRequest']
_GETLASTTRADESRESPONSE = DESCRIPTOR.message_types_by_name['GetLastTradesResponse']
MarketDataRequest = _reflection.GeneratedProtocolMessageType('MarketDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKETDATAREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.MarketDataRequest)
  })
_sym_db.RegisterMessage(MarketDataRequest)

MarketDataServerSideStreamRequest = _reflection.GeneratedProtocolMessageType('MarketDataServerSideStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKETDATASERVERSIDESTREAMREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.MarketDataServerSideStreamRequest)
  })
_sym_db.RegisterMessage(MarketDataServerSideStreamRequest)

MarketDataResponse = _reflection.GeneratedProtocolMessageType('MarketDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _MARKETDATARESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.MarketDataResponse)
  })
_sym_db.RegisterMessage(MarketDataResponse)

SubscribeCandlesRequest = _reflection.GeneratedProtocolMessageType('SubscribeCandlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECANDLESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequest)
  })
_sym_db.RegisterMessage(SubscribeCandlesRequest)

CandleInstrument = _reflection.GeneratedProtocolMessageType('CandleInstrument', (_message.Message,), {
  'DESCRIPTOR' : _CANDLEINSTRUMENT,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CandleInstrument)
  })
_sym_db.RegisterMessage(CandleInstrument)

SubscribeCandlesResponse = _reflection.GeneratedProtocolMessageType('SubscribeCandlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECANDLESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeCandlesResponse)
  })
_sym_db.RegisterMessage(SubscribeCandlesResponse)

CandleSubscription = _reflection.GeneratedProtocolMessageType('CandleSubscription', (_message.Message,), {
  'DESCRIPTOR' : _CANDLESUBSCRIPTION,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CandleSubscription)
  })
_sym_db.RegisterMessage(CandleSubscription)

SubscribeOrderBookRequest = _reflection.GeneratedProtocolMessageType('SubscribeOrderBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEORDERBOOKREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequest)
  })
_sym_db.RegisterMessage(SubscribeOrderBookRequest)

OrderBookInstrument = _reflection.GeneratedProtocolMessageType('OrderBookInstrument', (_message.Message,), {
  'DESCRIPTOR' : _ORDERBOOKINSTRUMENT,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderBookInstrument)
  })
_sym_db.RegisterMessage(OrderBookInstrument)

SubscribeOrderBookResponse = _reflection.GeneratedProtocolMessageType('SubscribeOrderBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEORDERBOOKRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeOrderBookResponse)
  })
_sym_db.RegisterMessage(SubscribeOrderBookResponse)

OrderBookSubscription = _reflection.GeneratedProtocolMessageType('OrderBookSubscription', (_message.Message,), {
  'DESCRIPTOR' : _ORDERBOOKSUBSCRIPTION,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderBookSubscription)
  })
_sym_db.RegisterMessage(OrderBookSubscription)

SubscribeTradesRequest = _reflection.GeneratedProtocolMessageType('SubscribeTradesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETRADESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeTradesRequest)
  })
_sym_db.RegisterMessage(SubscribeTradesRequest)

TradeInstrument = _reflection.GeneratedProtocolMessageType('TradeInstrument', (_message.Message,), {
  'DESCRIPTOR' : _TRADEINSTRUMENT,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.TradeInstrument)
  })
_sym_db.RegisterMessage(TradeInstrument)

SubscribeTradesResponse = _reflection.GeneratedProtocolMessageType('SubscribeTradesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETRADESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeTradesResponse)
  })
_sym_db.RegisterMessage(SubscribeTradesResponse)

TradeSubscription = _reflection.GeneratedProtocolMessageType('TradeSubscription', (_message.Message,), {
  'DESCRIPTOR' : _TRADESUBSCRIPTION,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.TradeSubscription)
  })
_sym_db.RegisterMessage(TradeSubscription)

SubscribeInfoRequest = _reflection.GeneratedProtocolMessageType('SubscribeInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEINFOREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeInfoRequest)
  })
_sym_db.RegisterMessage(SubscribeInfoRequest)

InfoInstrument = _reflection.GeneratedProtocolMessageType('InfoInstrument', (_message.Message,), {
  'DESCRIPTOR' : _INFOINSTRUMENT,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.InfoInstrument)
  })
_sym_db.RegisterMessage(InfoInstrument)

SubscribeInfoResponse = _reflection.GeneratedProtocolMessageType('SubscribeInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEINFORESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeInfoResponse)
  })
_sym_db.RegisterMessage(SubscribeInfoResponse)

InfoSubscription = _reflection.GeneratedProtocolMessageType('InfoSubscription', (_message.Message,), {
  'DESCRIPTOR' : _INFOSUBSCRIPTION,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.InfoSubscription)
  })
_sym_db.RegisterMessage(InfoSubscription)

SubscribeLastPriceRequest = _reflection.GeneratedProtocolMessageType('SubscribeLastPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBELASTPRICEREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequest)
  })
_sym_db.RegisterMessage(SubscribeLastPriceRequest)

LastPriceInstrument = _reflection.GeneratedProtocolMessageType('LastPriceInstrument', (_message.Message,), {
  'DESCRIPTOR' : _LASTPRICEINSTRUMENT,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.LastPriceInstrument)
  })
_sym_db.RegisterMessage(LastPriceInstrument)

SubscribeLastPriceResponse = _reflection.GeneratedProtocolMessageType('SubscribeLastPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBELASTPRICERESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SubscribeLastPriceResponse)
  })
_sym_db.RegisterMessage(SubscribeLastPriceResponse)

LastPriceSubscription = _reflection.GeneratedProtocolMessageType('LastPriceSubscription', (_message.Message,), {
  'DESCRIPTOR' : _LASTPRICESUBSCRIPTION,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.LastPriceSubscription)
  })
_sym_db.RegisterMessage(LastPriceSubscription)

Candle = _reflection.GeneratedProtocolMessageType('Candle', (_message.Message,), {
  'DESCRIPTOR' : _CANDLE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.Candle)
  })
_sym_db.RegisterMessage(Candle)

OrderBook = _reflection.GeneratedProtocolMessageType('OrderBook', (_message.Message,), {
  'DESCRIPTOR' : _ORDERBOOK,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OrderBook)
  })
_sym_db.RegisterMessage(OrderBook)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.Order)
  })
_sym_db.RegisterMessage(Order)

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), {
  'DESCRIPTOR' : _TRADE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.Trade)
  })
_sym_db.RegisterMessage(Trade)

TradingStatus = _reflection.GeneratedProtocolMessageType('TradingStatus', (_message.Message,), {
  'DESCRIPTOR' : _TRADINGSTATUS,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.TradingStatus)
  })
_sym_db.RegisterMessage(TradingStatus)

GetCandlesRequest = _reflection.GeneratedProtocolMessageType('GetCandlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCANDLESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetCandlesRequest)
  })
_sym_db.RegisterMessage(GetCandlesRequest)

GetCandlesResponse = _reflection.GeneratedProtocolMessageType('GetCandlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCANDLESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetCandlesResponse)
  })
_sym_db.RegisterMessage(GetCandlesResponse)

HistoricCandle = _reflection.GeneratedProtocolMessageType('HistoricCandle', (_message.Message,), {
  'DESCRIPTOR' : _HISTORICCANDLE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.HistoricCandle)
  })
_sym_db.RegisterMessage(HistoricCandle)

GetLastPricesRequest = _reflection.GeneratedProtocolMessageType('GetLastPricesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTPRICESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetLastPricesRequest)
  })
_sym_db.RegisterMessage(GetLastPricesRequest)

GetLastPricesResponse = _reflection.GeneratedProtocolMessageType('GetLastPricesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTPRICESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetLastPricesResponse)
  })
_sym_db.RegisterMessage(GetLastPricesResponse)

LastPrice = _reflection.GeneratedProtocolMessageType('LastPrice', (_message.Message,), {
  'DESCRIPTOR' : _LASTPRICE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.LastPrice)
  })
_sym_db.RegisterMessage(LastPrice)

GetOrderBookRequest = _reflection.GeneratedProtocolMessageType('GetOrderBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORDERBOOKREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetOrderBookRequest)
  })
_sym_db.RegisterMessage(GetOrderBookRequest)

GetOrderBookResponse = _reflection.GeneratedProtocolMessageType('GetOrderBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORDERBOOKRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetOrderBookResponse)
  })
_sym_db.RegisterMessage(GetOrderBookResponse)

GetTradingStatusRequest = _reflection.GeneratedProtocolMessageType('GetTradingStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRADINGSTATUSREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetTradingStatusRequest)
  })
_sym_db.RegisterMessage(GetTradingStatusRequest)

GetTradingStatusResponse = _reflection.GeneratedProtocolMessageType('GetTradingStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRADINGSTATUSRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetTradingStatusResponse)
  })
_sym_db.RegisterMessage(GetTradingStatusResponse)

GetLastTradesRequest = _reflection.GeneratedProtocolMessageType('GetLastTradesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTTRADESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetLastTradesRequest)
  })
_sym_db.RegisterMessage(GetLastTradesRequest)

GetLastTradesResponse = _reflection.GeneratedProtocolMessageType('GetLastTradesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTTRADESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.marketdata_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetLastTradesResponse)
  })
_sym_db.RegisterMessage(GetLastTradesResponse)

_MARKETDATASERVICE = DESCRIPTOR.services_by_name['MarketDataService']
_MARKETDATASTREAMSERVICE = DESCRIPTOR.services_by_name['MarketDataStreamService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _SUBSCRIPTIONACTION._serialized_start=8151
  _SUBSCRIPTIONACTION._serialized_end=8280
  _SUBSCRIPTIONINTERVAL._serialized_start=8283
  _SUBSCRIPTIONINTERVAL._serialized_end=8422
  _SUBSCRIPTIONSTATUS._serialized_start=8425
  _SUBSCRIPTIONSTATUS._serialized_end=8830
  _TRADEDIRECTION._serialized_start=8832
  _TRADEDIRECTION._serialized_end=8932
  _CANDLEINTERVAL._serialized_start=8935
  _CANDLEINTERVAL._serialized_end=9117
  _MARKETDATAREQUEST._serialized_start=147
  _MARKETDATAREQUEST._serialized_end=684
  _MARKETDATASERVERSIDESTREAMREQUEST._serialized_start=687
  _MARKETDATASERVERSIDESTREAMREQUEST._serialized_end=1219
  _MARKETDATARESPONSE._serialized_start=1222
  _MARKETDATARESPONSE._serialized_end=2182
  _SUBSCRIBECANDLESREQUEST._serialized_start=2185
  _SUBSCRIBECANDLESREQUEST._serialized_end=2399
  _CANDLEINSTRUMENT._serialized_start=2401
  _CANDLEINSTRUMENT._serialized_end=2512
  _SUBSCRIBECANDLESRESPONSE._serialized_start=2515
  _SUBSCRIBECANDLESRESPONSE._serialized_end=2652
  _CANDLESUBSCRIPTION._serialized_start=2655
  _CANDLESUBSCRIPTION._serialized_end=2856
  _SUBSCRIBEORDERBOOKREQUEST._serialized_start=2859
  _SUBSCRIBEORDERBOOKREQUEST._serialized_end=3055
  _ORDERBOOKINSTRUMENT._serialized_start=3057
  _ORDERBOOKINSTRUMENT._serialized_end=3107
  _SUBSCRIBEORDERBOOKRESPONSE._serialized_start=3110
  _SUBSCRIBEORDERBOOKRESPONSE._serialized_end=3255
  _ORDERBOOKSUBSCRIPTION._serialized_start=3258
  _ORDERBOOKSUBSCRIPTION._serialized_end=3398
  _SUBSCRIBETRADESREQUEST._serialized_start=3401
  _SUBSCRIBETRADESREQUEST._serialized_end=3590
  _TRADEINSTRUMENT._serialized_start=3592
  _TRADEINSTRUMENT._serialized_end=3623
  _SUBSCRIBETRADESRESPONSE._serialized_start=3626
  _SUBSCRIBETRADESRESPONSE._serialized_end=3759
  _TRADESUBSCRIPTION._serialized_start=3761
  _TRADESUBSCRIPTION._serialized_end=3882
  _SUBSCRIBEINFOREQUEST._serialized_start=3885
  _SUBSCRIBEINFOREQUEST._serialized_end=4071
  _INFOINSTRUMENT._serialized_start=4073
  _INFOINSTRUMENT._serialized_end=4103
  _SUBSCRIBEINFORESPONSE._serialized_start=4106
  _SUBSCRIBEINFORESPONSE._serialized_end=4235
  _INFOSUBSCRIPTION._serialized_start=4237
  _INFOSUBSCRIPTION._serialized_end=4357
  _SUBSCRIBELASTPRICEREQUEST._serialized_start=4360
  _SUBSCRIBELASTPRICEREQUEST._serialized_end=4556
  _LASTPRICEINSTRUMENT._serialized_start=4558
  _LASTPRICEINSTRUMENT._serialized_end=4593
  _SUBSCRIBELASTPRICERESPONSE._serialized_start=4596
  _SUBSCRIBELASTPRICERESPONSE._serialized_end=4741
  _LASTPRICESUBSCRIPTION._serialized_start=4743
  _LASTPRICESUBSCRIPTION._serialized_end=4868
  _CANDLE._serialized_start=4871
  _CANDLE._serialized_end=5337
  _ORDERBOOK._serialized_start=5340
  _ORDERBOOK._serialized_end=5703
  _ORDER._serialized_start=5705
  _ORDER._serialized_end=5795
  _TRADE._serialized_start=5798
  _TRADE._serialized_end=6018
  _TRADINGSTATUS._serialized_start=6021
  _TRADINGSTATUS._serialized_end=6251
  _GETCANDLESREQUEST._serialized_start=6254
  _GETCANDLESREQUEST._serialized_end=6442
  _GETCANDLESRESPONSE._serialized_start=6444
  _GETCANDLESRESPONSE._serialized_end=6536
  _HISTORICCANDLE._serialized_start=6539
  _HISTORICCANDLE._serialized_end=6890
  _GETLASTPRICESREQUEST._serialized_start=6892
  _GETLASTPRICESREQUEST._serialized_end=6928
  _GETLASTPRICESRESPONSE._serialized_start=6930
  _GETLASTPRICESRESPONSE._serialized_end=7024
  _LASTPRICE._serialized_start=7027
  _LASTPRICE._serialized_end=7159
  _GETORDERBOOKREQUEST._serialized_start=7161
  _GETORDERBOOKREQUEST._serialized_end=7211
  _GETORDERBOOKRESPONSE._serialized_start=7214
  _GETORDERBOOKRESPONSE._serialized_end=7664
  _GETTRADINGSTATUSREQUEST._serialized_start=7666
  _GETTRADINGSTATUSREQUEST._serialized_end=7705
  _GETTRADINGSTATUSRESPONSE._serialized_start=7708
  _GETTRADINGSTATUSRESPONSE._serialized_end=7941
  _GETLASTTRADESREQUEST._serialized_start=7943
  _GETLASTTRADESREQUEST._serialized_end=8061
  _GETLASTTRADESRESPONSE._serialized_start=8063
  _GETLASTTRADESRESPONSE._serialized_end=8148
  _MARKETDATASERVICE._serialized_start=9120
  _MARKETDATASERVICE._serialized_end=9841
  _MARKETDATASTREAMSERVICE._serialized_start=9844
  _MARKETDATASTREAMSERVICE._serialized_end=10177
# @@protoc_insertion_point(module_scope)
