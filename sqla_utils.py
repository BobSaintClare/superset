import logging
from sqlalchemy import event

def trace_db_events(logger, db_engine):
	@event.listens_for(db_engine.pool, 'checkin')
	def receive_checkin(dbapi_connection, connection_record):
	    logger.info("trace_db_events - db_engine.pool - CHECKIN")

	@event.listens_for(db_engine.pool, 'checkout')
	def receive_checkout(dbapi_connection, connection_record, connection_proxy):
	    logger.info("trace_db_events - db_engine.pool - CHECKOUT")

	# @event.listens_for(db_engine.pool, 'close')
	# def receive_close(dbapi_connection, connection_record):
	#     logger.info("trace_db_events - db_engine.pool - CLOSE")

	# @event.listens_for(db_engine.pool, 'close_detached')
	# def receive_close_detached(dbapi_connection):
	#     logger.info("trace_db_events - db_engine.pool - CLOSE_DETACHED")

	@event.listens_for(db_engine.pool, 'connect')
	def receive_connect(dbapi_connection, connection_record):
	    logger.info("trace_db_events - db_engine.pool - CONNECT")

	# @event.listens_for(db_engine.pool, 'detach')
	# def receive_detach(dbapi_connection, connection_record):
	#     logger.info("trace_db_events - db_engine.pool - DETACHED")

	@event.listens_for(db_engine.pool, 'first_connect')
	def receive_first_connect(dbapi_connection, connection_record):
	    logger.info("trace_db_events - db_engine.pool - FIRST_CONNECT")

	@event.listens_for(db_engine.pool, 'invalidate')
	def receive_invalidate(dbapi_connection, connection_record, exception):
	    logger.info("trace_db_events - db_engine.pool - INVALIDATE")

	@event.listens_for(db_engine.pool, 'reset')
	def receive_reset(dbapi_connection, connection_record):
	    logger.info("trace_db_events - db_engine.pool - RESET")

	@event.listens_for(db_engine.pool, 'soft_invalidate')
	def receive_soft_invalidate(dbapi_connection, connection_record, exception):
	    logger.info("trace_db_events - db_engine.pool - SOFT_INVALIDATE")


	# @event.listens_for(db_engine, 'before_cursor_execute')
	# def receive_before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
	#     logger.info("trace_db_events - db_engine - before_cursor_execute")

	# @event.listens_for(db_engine, 'before_execute')
	# def receive_before_execute(conn, clauseelement, multiparams, params):
	#     logger.info("trace_db_events - db_engine - before_execute")

	@event.listens_for(db_engine, 'begin')
	def receive_begin(conn):
	    logger.info("trace_db_events - db_engine - begin")

	# @event.listens_for(db_engine, 'begin_twophase')
	# def receive_begin_twophase(conn, xid):
	#     logger.info("trace_db_events - db_engine - begin_twophase")

	@event.listens_for(db_engine, 'dbapi_error')
	def receive_dbapi_error(conn, cursor, statement, parameters, context, exception):
	    logger.info("trace_db_events - db_engine - dbapi_error")

	@event.listens_for(db_engine, 'engine_connect')
	def receive_engine_connect(conn, branch):
	    logger.info("trace_db_events - db_engine - engine_connect")

	@event.listens_for(db_engine, 'engine_disposed')
	def receive_engine_disposed(engine):
	    logger.info("trace_db_events - db_engine - engine_disposed")

	@event.listens_for(db_engine, 'handle_error')
	def receive_handle_error(exception_context):
	    logger.info("trace_db_events - db_engine - handle_error")

	@event.listens_for(db_engine, 'prepare_twophase')
	def receive_prepare_twophase(conn, xid):
	    logger.info("trace_db_events - db_engine - prepare_twophase")

	@event.listens_for(db_engine, 'rollback')
	def receive_rollback(conn):
	    logger.info("trace_db_events - db_engine - rollback")

	@event.listens_for(db_engine, 'rollback_twophase')
	def receive_rollback_twophase(conn, xid, is_prepared):
	    logger.info("trace_db_events - db_engine - rollback_twophase")


	@event.listens_for(db_engine, 'set_connection_execution_options')
	def receive_set_connection_execution_options(conn, opts):
	    logger.info("trace_db_events - db_engine - set_connection_execution_options")

	@event.listens_for(db_engine, 'set_engine_execution_options')
	def receive_set_engine_execution_options(engine, opts):
	    logger.info("trace_db_events - db_engine - set_engine_execution_options")

	@event.listens_for(db_engine, 'do_connect')
	def receive_do_connect(dialect, conn_rec, cargs, cparams):
	    logger.info("trace_db_events - db_engine - do_connect")

	# @event.listens_for(db_engine, 'do_execute')
	# def receive_do_execute(cursor, statement, parameters, context):
	#     logger.info("trace_db_events - db_engine - do_execute")

