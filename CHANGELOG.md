# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.8.0...HEAD)

## [0.8.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.7.1...v0.8.0) - 2026-11-17
### Changed
- Save streaming records into a PostgreSQL database.

## [0.7.1](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.7.0...v0.7.1) - 2026-11-16
### Fixed
- Use a more complex location structure for message location consisting of `latitude, longitude, location_name, country_code, timezone`.

## [0.7.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.6.0...v0.7.0) - 2026-11-09
### Changed
- The PySpark streaming now performs a simple sentiment analysis using [library `vadersentiment`](https://vadersentiment.readthedocs.io/en/latest/) on the messages coming from Kakfa.

## [0.6.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.5.0...v0.6.0) - 2026-11-08
### Added
- Simple initial PySpark streaming script to read messages in a Kafka topic.
- Docker container holding the execution of the script.

## [0.5.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.4.0...v0.5.0) - 2026-11-07
### Added
- Add PostgreSQL container to `docker-compose.yml` so that further analytics results can be collected there.

## [0.4.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.3.0...v0.4.0) - 2026-11-03
### Added
- Python scripts to send messages to a Kafka cluster.
- Add more infrastructure to docker-ize the Python application for message sending to another Kafka running container.

## [0.3.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.2.0...v0.3.0) - 2026-10-30
### Added
- Initial infrastructure through Docker compose to bring up a Kafka cluster.

## [0.2.0](https://github.com/glapuente/tweet_sentiment_analysis/compare/v0.1.0...v0.2.0) - 2026-10-25
### Added
- Scaffolding of the project structure.
- Initial offline Tweet fetcher from a static CSV file.

## [0.1.0](https://github.com/glapuente/tweet_sentiment_analysis/releases/tag/v0.1.0) - 2026-10-16
### Added
- Initial commit of the project mainly with documentation.
