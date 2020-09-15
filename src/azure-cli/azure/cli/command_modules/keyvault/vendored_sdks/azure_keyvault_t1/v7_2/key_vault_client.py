# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: skip-file
# flake8: noqa
import json

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling
import uuid
from . import models


class KeyVaultClientConfiguration(AzureConfiguration):
    """Configuration for KeyVaultClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    """

    def __init__(
            self, credentials):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{vaultBaseUrl}'

        super(KeyVaultClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-keyvault/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class KeyVaultClient(SDKClient):
    """The key vault client performs cryptographic key operations and vault operations against the Key Vault service.

    :ivar config: Configuration for client.
    :vartype config: KeyVaultClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    """

    def __init__(
            self, credentials):

        self.config = KeyVaultClientConfiguration(credentials)
        super(KeyVaultClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '7.2'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    def download(self, vault_base_url, certificates, custom_headers=None, raw=False, **operation_config):
        """Retrieves Security domain from HSM enclave.
        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param certificates: Security domain download operation requires customer to provide three
         certificates containing public key in JWK format.
        :type certificates: ~key_vault_client.models.CertificateSet
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityDomainObject, or the result of cls(response)
        :rtype: ~key_vault_client.models.SecurityDomainObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        # Construct URL
        url = self.download.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(certificates, 'CertificateSet')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        request.body = json.dumps(body_content)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SecurityDomainObject', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    download.metadata = {'url': '/securitydomain/download'}

    def transfer_key(self, vault_base_url, custom_headers=None, raw=False, **operation_config):
        """Retrieve security domain transfer key.
        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TransferKey, or the result of cls(response)
        :rtype: ~key_vault_client.models.TransferKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        # Construct URL
        url = self.transfer_key.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(
            request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = response.text

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    transfer_key.metadata = {'url': '/securitydomain/upload'}

    def upload(self, vault_base_url, security_domain, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self._upload_initial.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(security_domain, 'SecurityDomainObject')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        request.body = json.dumps(body_content)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    upload.metadata = {'url': '/securitydomain/upload'}

    def upload_pending(self, vault_base_url, custom_headers=None, raw=False, **operation_config):
        """Get Security domain upload operation status.
        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityDomainOperationStatus, or the result of cls(response)
        :rtype: ~key_vault_client.models.SecurityDomainOperationStatus
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        # Construct URL
        url = self.upload_pending.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(
            request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SecurityDomainOperationStatus', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upload_pending.metadata = {'url': '/securitydomain/upload/pending'}

    def _upload_initial(
            self, vault_base_url, security_domain, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self._upload_initial.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(security_domain, 'SecurityDomainObject')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        request.body = json.dumps(body_content)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    _upload_initial.metadata = {'url': '/securitydomain/upload'}

    def begin_upload(self, vault_base_url, security_domain, custom_headers=None, raw=False, polling=True, **operation_config):
        """Request Security domain upload operation.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param security_domain: security domain.
        :type security_domain: ~key_vault_client.models.SecurityDomainObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either SecurityDomainOperationStatus or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~key_vault_client.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        raw_result = self._upload_initial(
            vault_base_url=vault_base_url,
            security_domain=security_domain,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True:
            polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)